import heapq  # 우선순위 큐 사용

def solution(maps):
    N = len(maps)       # 맵의 행 개수
    M = len(maps[0])    # 맵의 열 개수
    
    # Manhattan distance를 계산하는 휴리스틱 함수
    def heuristic(r, c):
        return abs((N - 1) - r) + abs((M - 1) - c)
    
    # 각 좌표까지 도달하는데 걸린 실제 비용을 저장할 2차원 리스트 (초기값: 무한대)
    cost = [[float('inf')] * M for _ in range(N)]
    cost[0][0] = 1    # 시작점의 비용
    
    # 우선순위 큐 초기화: (총 예상 비용, 현재까지의 비용, r, c)
    heap = []
    heapq.heappush(heap, (1 + heuristic(0, 0), 1, 0, 0))
    
    # 우선순위 큐가 빌 때까지 A* 탐색 수행
    while heap:
        f, cur_cost, r, c = heapq.heappop(heap)
        # 목표 지점에 도달했다면 현재까지의 비용 반환
        if r == N - 1 and c == M - 1:
            return cur_cost
        
        # 상하좌우 4방향 탐색
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            # 맵 내부이고, 벽이 아니라면
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc]:
                next_cost = cur_cost + 1
                # 더 짧은 경로를 찾은 경우
                if next_cost < cost[nr][nc]:
                    cost[nr][nc] = next_cost
                    heapq.heappush(heap, (next_cost + heuristic(nr, nc), next_cost, nr, nc))
    
    # 목표 지점에 도달하지 못한 경우 -1 반환
    return -1