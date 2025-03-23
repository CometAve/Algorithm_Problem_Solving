import sys
from collections import Counter
input = sys.stdin.readline
MOD = 1000000007

n = int(input())
a = list(map(int, input().split()))
m = max(a)

# 원래 각 열의 위치 기여: 열 i에 a[i]개의 구슬이 있으므로 i*a[i]의 합
ori_sum = 0
for i, val in enumerate(a):
    ori_sum = (ori_sum + i * val) % MOD

# a의 고유값별 빈도를 구한 후, 오름차순으로 정렬 (높이가 증가할 때 count는 감소함)
from collections import Counter
freq = Counter(a)
distinct = sorted(freq.keys())

S = 0
prev = 0
r = 0  # 현재까지 처리한(작은 값의) 개수. 
# h(높이)는 1부터 m까지 변화하는데, a[i]>=h인 열의 개수는 h가 일정 구간에서는 일정하다.
for v in distinct:
    # 이전 고유값(prev)보다 크고 v 이하인 모든 h에 대해 count는 n - r
    L = v - prev  # h 값의 개수 (prev+1 부터 v까지)
    c = n - r    # 해당 구간에서 a[i]>=h 인 열의 개수
    # 해당 높이에서 최종 위치의 합: c*(n-c) + c*(c-1)//2
    term = (c * (n - c) + c * (c - 1) // 2) % MOD
    S = (S + L * term) % MOD
    r += freq[v]
    prev = v

total_distance = (S - ori_sum) % MOD
print(total_distance)