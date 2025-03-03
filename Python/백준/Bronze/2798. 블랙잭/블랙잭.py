# combination 사용하지 않은 버전

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            current_sum = arr[i] + arr[j] + arr[k]
            if max_sum < current_sum <= M:
                max_sum = current_sum

print(max_sum)