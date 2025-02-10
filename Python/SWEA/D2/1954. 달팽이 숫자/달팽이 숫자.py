T = int(input())

def create_snail(N):
    snail = [[0] * N for _ in range(N)]

    x, y = 0, 0 # 시작점
    d = 0 # 현재 방향 우 :1, 하 :2, 좌 :3, 상 :4
    dx = [0, 1, 0, -1] # 방향 벡터
    dy = [1, 0, -1, 0]

    # 1부터 N*N까지 숫자를 채워넣는다.
    for i in range(1, N * N + 1):
        snail[x][y] = i
        nx, ny = x + dx[d], y + dy[d]

        # 다음 위치가 범위를 벗어나거나 이미 숫자가 채워져 있으면 방향을 바꿔준다.
        if not (0 <= nx < N and 0 <= ny < N) or snail[nx][ny]:
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]

        x, y = nx, ny

    return snail

for test_case in range(1, T + 1):
    N = int(input())
    result = create_snail(N)

    print(f'#{test_case}')
    for i in result:
        print(*i)