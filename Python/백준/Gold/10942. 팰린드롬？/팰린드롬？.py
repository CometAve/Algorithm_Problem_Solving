# Manacher 알고리즘을 이용한 풀이
# 홀수 길이 팰린드롬과 짝수 길이 팰린드롬을 따로 계산
# 팰린드롬 반지름을 계산하면서 질문에 대한 답을 찾음
# 시간 복잡도: O(N + M)
import sys
input = sys.stdin.readline

def manacher_odd(arr, n):
    palindrome_radius = [0] * n  # 각 위치에서 팰린드롬의 반지름
    center, right_boundary = 0, -1  # 현재 팰린드롬의 중심과 오른쪽 경계
    
    for i in range(n):
        # 현재 위치가 이전에 발견된 팰린드롬 내에 있는지 확인
        if i <= right_boundary:
            # 대칭 위치의 반지름과 현재 팰린드롬 내 남은 거리 중 작은 값으로 초기화
            radius = min(palindrome_radius[center*2 - i], right_boundary - i + 1)
        else:
            radius = 1  # 새로운 위치에서 시작
            
        # 팰린드롬 확장 시도
        while 0 <= i-radius and i+radius < n and arr[i-radius] == arr[i+radius]:
            radius += 1
            
        palindrome_radius[i] = radius
        
        # 현재 팰린드롬이 이전 오른쪽 경계를 넘어가면 중심과 경계 업데이트
        if i + radius - 1 > right_boundary:
            center, right_boundary = i, i + radius - 1
            
    return palindrome_radius

def manacher_even(arr, n):
    palindrome_radius = [0] * n  # 각 위치에서 짝수 길이 팰린드롬의 반길이
    center, right_boundary = 0, -1
    
    for i in range(n):
        if i <= right_boundary:
            radius = min(palindrome_radius[center*2 - i + 1], right_boundary - i + 1)
        else:
            radius = 0  # 짝수 길이는 0부터 시작 (중심점이 두 글자 사이에 있음)
            
        # 짝수 길이 팰린드롬은 i와 i-1 위치를 대칭으로 확장
        while 0 <= i-radius-1 and i+radius < n and arr[i-radius-1] == arr[i+radius]:
            radius += 1
            
        palindrome_radius[i] = radius
        
        if i + radius - 1 > right_boundary:
            center, right_boundary = i, i + radius - 1
            
    return palindrome_radius

def solve():
    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())
    
    # Manacher 알고리즘으로 모든 가능한 팰린드롬 미리 계산
    odd_palindromes = manacher_odd(numbers, N)
    even_palindromes = manacher_even(numbers, N)
    
    # 각 질문에 대한 결과 저장
    results = [''] * M
    
    for i in range(M):
        start, end = map(int, input().split())
        start -= 1  # 0-인덱스로 변환
        end -= 1
        length = end - start + 1
        
        # 구간의 길이에 따라 적절한 검증 방법 선택
        if length == 1:
            # 길이가 1인 경우 항상 팰린드롬
            results[i] = '1'
        elif length % 2 == 1:
            # 홀수 길이 팰린드롬 확인
            center = (start + end) // 2
            # 필요한 반지름이 실제 팰린드롬 반지름보다 작거나 같은지 확인
            results[i] = '1' if odd_palindromes[center] >= (length+1)//2 else '0'
        else:
            # 짝수 길이 팰린드롬 확인
            center = (start + end + 1) // 2
            # 필요한 반길이가 실제 팰린드롬 반길이보다 작거나 같은지 확인
            results[i] = '1' if even_palindromes[center] >= length//2 else '0'
    
    sys.stdout.write('\n'.join(results))

if __name__ == "__main__":
    solve()