T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
 
    snail = [[0] * N for _ in range(N) for _ in range(N)]
 
    # 우 하 좌 상
    d = 0
 
    # 우 = 0, 하 = 1, 좌 = 2, 상 = 3
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
 
    # 시작점
    x, y = 0, 0
 
    # 1부터 가로 N까지 숫자 채우기
    for i in range(1, N * N + 1):
        snail[x][y] = i
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x = x + dx[d]
            y = y + dy[d]
 
    print(f'#{test_case}')
    for i in range(N):
        print(*snail[i])