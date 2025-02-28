T = int(input())

for tc in range(1, T + 1):

    # 필요 데이터
    # N * N의 맵 크기
    N = int(input())
    # 구역을 받을 입력 N * N 크기의 맵
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 1: 벽, 2: 외계인
    # 외계인의 광선은 벽이 없으면 본인의 위치에서 상하좌우 끝까지 뻗어간다.
    # 광선이 뻗어 나가다가 벽을 만나면 멈춤
    # 안전영역의 개수 (만약 안전영역이 없을 경우가 있을 수 있으니 0)
    cnt = 0

    # 로직
    # 1. 우주 괴물의 위치 파악
    # 1-1. for N*N을 돌면서 2를 만나면 중지 위치 저장
    # 괴물 위치를 저장해줄 변수
    r = c = -1
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                r, c = i, j
                break
        # 완전히 탐색을 멈추기 위해서 r이 더 이상 -1이 아니면 스탑
        if r != -1:
            break
    # 2. 괴물의 위치를 기반으로 상하좌우에 값을 넣어둠 3으로 넣어둠
    # 2-1. 델타탐색 상하좌우에 기록하다가 1을 만나기 전까지
    # 2-2. 벽을 만나기 전까지
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        while 0 <= nr < N and 0 <= nc < N:
            if graph[nr][nc] == 1:
                break
            graph[nr][nc] += 3
            nr += dr[d]
            nc += dc[d]

    # 3. 다시 for N*N을 돌면서 안전구역 0의 개수를 기록
    for i in range(N):
        cnt += graph[i].count(0)

    print(f'#{tc} {cnt}')