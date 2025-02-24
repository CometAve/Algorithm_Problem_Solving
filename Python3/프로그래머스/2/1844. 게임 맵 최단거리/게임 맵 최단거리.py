from collections import deque  # FIFO 큐 사용을 위한 collections 모듈의 deque 임포트

def solution(maps):
    N = len(maps)          # 맵의 행(row)의 개수를 저장
    M = len(maps[0])       # 맵의 열(column)의 개수를 저장
    visited = [[0] * M for _ in range(N)]  # 각 칸을 방문했는지 기록하는 2차원 리스트 초기화

    q = deque()            # BFS를 위한 큐 생성
    q.append((0, 0))       # 시작 지점 (0, 0)을 큐에 추가
    visited[0][0] = 1      # 시작 지점을 방문 처리

    # 큐가 빌 때까지 BFS 실행
    while q:
        r, c = q.popleft()  # 현재 위치 (r, c)를 큐에서 꺼냄

        # 상하좌우 네 방향으로 이동
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = r + dr  # 다음 행 좌표 계산
            nc = c + dc  # 다음 열 좌표 계산
            # 다음 좌표가 맵의 범위 내에 있고, 벽이 아니면(예: maps 값이 1이면 길이다)
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc]:
                # 아직 방문하지 않은 칸이라면
                if not visited[nr][nc]:
                    visited[nr][nc] = 1           # 해당 칸을 방문했다고 기록
                    q.append((nr, nc))            # 해당 칸을 큐에 추가하여 탐색 진행
                    maps[nr][nc] = maps[r][c] + 1   # 현재 칸의 거리 값에서 1을 더해 다음 칸의 최단 거리 기록

    # 목적지(오른쪽 아래 모서리)에 도달했는지 확인: 값이 1이면 도달하지 못한 것이므로 -1 반환
    if maps[N - 1][M - 1] == 1:
        return -1
    else:
        return maps[N - 1][M - 1]  # 목적지까지 도달한 최단 거리 반환