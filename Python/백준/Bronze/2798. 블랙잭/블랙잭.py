import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0

for i in combinations(arr, 3):
    if max_sum < sum(i) <= M:
        current_sum = sum(i)
        max_sum = sum(i)

print(max_sum)