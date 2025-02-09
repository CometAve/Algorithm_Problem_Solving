import sys
input = sys.stdin.readline

# 수의 개수 (1 <= N <= 10,000,000)
N = int(input())

# 카운트 배열 생성
number_count = [0] * 10001

# 입력과 동시에 카운트 배열에 저장
for _ in range(N):
    number = int(input())
    number_count[number] += 1

# 카운트 배열을 순회하면서
# 0이 아닌 원소를 발견하면
# 해당 인덱스를 원소만큼 출력
for i in range(10001):
    if number_count[i] != 0:
        for j in range(number_count[i]):
            print(f'{i}', end='\n')



# --------------------------------
"""
메모리 초과된 나의 풀이법(카운트 정렬, 버블 정렬)

# N : 수의 개수 (1 <= N <= 10,000,000)
N = int(input())

# 수들을 한 줄씩 받으며 리스트에다가 추가
number_list = []
for i in range(N):
    number = int(input())
    number_list.append(number)

# 주어진 조건
# 각 수들은 <= 10,000

# 내장함수 sorted로 오름차순 정렬
number_list = sorted(number_list)

# 버블 정렬로 오름차순으로 정렬 (메모리 초과)
for i in range(N-1, 0, -1):
    for j in range(i):
        if number_list[j] > number_list[j+1]:
            number_list[j], number_list[j+1] = number_list[j+1], number_list[j]


# 카운트 정렬 사용
# 카운트 배열 생성
number_count = [0] * 10001

# 각 수들의 등장 횟수를 카운트 배열에 저장
for number in number_list:
    number_count[number] += 1
    
# 오름차순으로 정렬하기 위해
# count 배열에서 자신의 앞 수들의 등장 횟수 누적합
for i in range(1, 10001):
    number_count[i] += number_count[i-1]

# 오름차순 결과를 담을 새로운 리스트
sorted_number_list = [0] * N

# 뒤에서부터 number_list를 확인하면서
# count 배열을 보고 자리 확인 후
# count 배열에 해당 원소 -1
for i in range(N-1, -1 ,-1):
    number_count[number_list[i]] -= 1
    
    sorted_number_list[number_count[number_list[i]]] = number_list[i]

# 한 줄에 하나씩 출력
for i in sorted_number_list:
    print(i)
    
"""
# -----------------------------