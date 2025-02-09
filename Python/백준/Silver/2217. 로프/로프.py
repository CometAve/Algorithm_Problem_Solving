# 내장 함수를 사용하지 않고
# 최적화 접근 풀이

import sys
input = sys.stdin.readline

N = int(input())

# 각 로프들의 중량을 카운팅할 리스트
count_list = [0] * 10001

# 입력과 동시에 카운팅
for _ in range(N):
    count_list[int(input())] += 1

# rope_list를 만들지 않고 바로 최대 중량 계산
max_weight = 0
current_ropes = 0

# 내림차순으로 순회하면서 계산
for weight in range(10000, 0, -1):
    if count_list[weight]:
        # 로프개수를 누적하여 최대 중량을 계산
        rope_count = count_list[weight]
        current_ropes += rope_count
        possible_weight = weight * current_ropes
        if possible_weight > max_weight:
            max_weight = possible_weight
        
print(max_weight)


"""
시간초과된 풀이법
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
        
시간초과 문제 해결(카운트 정렬)
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
"""