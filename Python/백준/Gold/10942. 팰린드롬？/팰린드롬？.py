# 문제 해결 방법
# dp를 이용하여 팰린드롬인지 아닌지를 확인한다.
# dp[i][j] = i부터 j까지의 부분 수열이 팰린드롬인지 아닌지를 저장한다.
# 길이가 1인 부분 수열은 항상 팰린드롬이다.
# 길이가 2인 부분 수열은 두 수가 같으면 팰린드롬이다.
# 길이가 3 이상인 부분 수열은 양 끝의 수가 같고, 그 사이의 부분 수열이 팰린드롬이면 팰린드롬이다.
# S와 E가 주어졌을 때, dp[S-1][E-1]을 출력하면 된다.

import sys

def main():
    data = sys.stdin.read().split()
    t = 0
    N = int(data[t]); t += 1
    arr = list(map(int, data[t:t+N])); t += N
    M = int(data[t]); t += 1

    dp = [[0] * N for _ in range(N)]
    
    # 길이 1: 항상 팰린드롬
    for i in range(N):
        dp[i][i] = 1

    # 길이 2인 부분 수열 확인
    for i in range(N-1):
        if arr[i] == arr[i+1]:
            dp[i][i+1] = 1

    # 길이 3 이상인 부분 수열 확인
    for length in range(3, N+1):
        for start in range(N - length + 1):
            end = start + length - 1
            if arr[start] == arr[end] and dp[start+1][end-1]:
                dp[start][end] = 1

    answer = []
    for _ in range(M):
        S = int(data[t]); E = int(data[t+1]); t += 2
        answer.append(str(dp[S-1][E-1]))

    sys.stdout.write('\n'.join(answer))

if __name__ == '__main__':
    main()