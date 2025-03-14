# 상하좌우 방향 이동을 위한 델타 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 수열 저장할 배열
    array = [0] * (N * N + 1)
    max_cnt = 0
    idx = 0 # 이동할 수 있는 방의 개수가 최대인 방의 번호
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N and rooms[nx][ny] == rooms[i][j] + 1:
                    array[rooms[i][j]] = 1
                    break
    
    # 이동할 수 있는 방의 개수를 구한다.
    cnt = 1
    for i in range(1, N*N+1):
        if array[i] == 1:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                idx = i - cnt
            cnt = 1

    if cnt > max_cnt:
        max_cnt = cnt
        idx = i - cnt
    
    print(f'#{tc} {idx+1} {max_cnt}')