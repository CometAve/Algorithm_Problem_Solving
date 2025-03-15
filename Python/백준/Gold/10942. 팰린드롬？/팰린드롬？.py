import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# DP 배열 초기화
dp = [[0] * N for _ in range(N)]

# 길이 1인 부분 수열은 항상 팰린드롬
for i in range(N):
    dp[i][i] = 1

# 길이 2인 부분 수열 확인
for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상인 부분 수열 확인 - 더 효율적인 순회 방식
for length in range(3, N+1):
    for start in range(N-length+1):
        end = start + length - 1
        if arr[start] == arr[end] and dp[start+1][end-1]:
            dp[start][end] = 1

# 질문 결과를 한 번에 모아서 출력
answer = []
for _ in range(M):
    S, E = map(int, input().split())
    answer.append(str(dp[S-1][E-1]))

# 한 번에 출력하는 것이 여러 번 write 호출보다 효율적
sys.stdout.write('\n'.join(answer))