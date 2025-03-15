import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
    if i < N - 1 and arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N):
    for j in range(N - i):
        if arr[j] == arr[j + i] and dp[j + 1][j + i - 1]:
            dp[j][j + i] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(f"{dp[S - 1][E - 1]}\n")