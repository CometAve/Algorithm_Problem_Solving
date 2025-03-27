# 문제 해결
# DP와 비트마스크를 이용해 풀 수 있는 문제이다.
# DP[현재 도시][방문한 도시들]로 정의하자.
# DP[현재 도시][방문한 도시들] = min(DP[현재 도시][방문한 도시들], DP[이전 도시][방문한 도시들] + W[이전 도시][현재 도시])
# 이때, 방문한 도시들은 비트마스크로 표현할 수 있다.

import sys
input = sys.stdin.readline
INF = sys.maxsize

def tsp(cur, visited, N, W, dp):
    if visited == (1 << N) - 1:
        return W[cur][0] if W[cur][0] != 0 else INF

    if dp[cur][visited] != -1:
        return dp[cur][visited]

    dp[cur][visited] = INF
    for i in range(1, N):
        if W[cur][i] == 0 or visited & (1 << i):
            continue
        dp[cur][visited] = min(dp[cur][visited], tsp(i, visited | (1 << i), N, W, dp) + W[cur][i])

    return dp[cur][visited]

def solve():
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * (1 << N) for _ in range(N)]
    sys.stdout.write(str(tsp(0, 1, N, W, dp)))

if __name__ == '__main__':
    solve()