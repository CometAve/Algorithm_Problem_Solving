def fast_solve():
    max_sum = 0
    for i in range(N):
        for j in range(M):
            dist = board[i][j]
            current = dist
            for k in range(1, dist + 1):
                # 상하좌우를 한번에 처리
                if i - k >= 0: current += board[i-k][j]
                if i + k < N: current += board[i+k][j]
                if j - k >= 0: current += board[i][j-k]
                if j + k < M: current += board[i][j+k]
            
            max_sum = max(max_sum, current)
    return max_sum

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {fast_solve()}')