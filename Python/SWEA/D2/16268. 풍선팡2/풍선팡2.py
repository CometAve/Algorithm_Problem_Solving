def get_max_sum():
    max_sum = 0
    for i in range(N):
        for j in range(M):
            current = board[i][j]
             
            # 한 번의 순회로 상하좌우 처리
            for k in range(1,2):
                # 상하
                if i - k >= 0: current += board[i-k][j]
                if i + k < N: current += board[i+k][j]
                # 좌우
                if j - k >= 0: current += board[i][j-k]
                if j + k < M: current += board[i][j+k]
                     
            max_sum = max(max_sum, current)
    return max_sum
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {get_max_sum()}')