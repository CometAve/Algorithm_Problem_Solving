import sys
input = sys.stdin.readline

# N : 주어진 로프의 개수 (1 <= N <= 100,000)
N = int(input())
count_list = [0] * 10001

# 카운팅 정렬을 이용하여 로프들의 중량을 입력받음
for _ in range(N):
    count_list[int(input())] += 1

# 로프들의 중량을 내림차순으로 정렬
rope_list = []
for i in range(10000, 0, -1):
    if count_list[i]:
        rope_list.extend([i] * count_list[i])

# 로프들의 중량을 내림차순으로 정렬했으므로
# 각 로프들의 중량에 해당 인덱스 + 1를 곱한 값 중
# 가장 큰 값을 출력
max_weight = 0
for i in range(1, N+1):
    current_weight = rope_list[i-1] * i
    if current_weight > max_weight:
        max_weight = current_weight

print(max_weight)


"""
시간초과 풀이
# 로프들의 중량을 담을 리스트
rope_list = []
for _ in range(N):
    rope_list.append(int(input()))
    
# 삽입정렬을 통해 로프들의 중량을 내림차순으로 정렬
for j in range(len(rope_list)-1, 0, -1):
    if rope_list[j] > rope_list[j-1]:
        rope_list[j], rope_list[j-1] = rope_list[j-1], rope_list[j]
    else:
        break
"""