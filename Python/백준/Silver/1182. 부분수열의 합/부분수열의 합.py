import sys
input = sys.stdin.readline

# 입력 처리
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 부분수열의 합이 s인 경우의 수
count = 0

# 1부터 시작하여 공집합 제외(양수 크기부터)
for i in range(1, 1 << n):  # 1 << n은 2^n을 의미
    current_sum = 0
    
    # 현재 비트마스크에 해당하는 부분수열 생성
    for j in range(n):
        # i의 j번째 비트가 1이면 arr[j]를 부분수열에 포함
        if i & (1 << j):
            current_sum += arr[j]
    
    # 부분수열의 합이 s와 같으면 카운트 증가
    if current_sum == s:
        count += 1

print(count)