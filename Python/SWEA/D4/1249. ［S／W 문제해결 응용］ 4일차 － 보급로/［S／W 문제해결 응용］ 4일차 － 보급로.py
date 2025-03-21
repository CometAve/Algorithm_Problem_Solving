import heapq
INF = int(1e9)
def dijkstra(start_x, start_y):
    q = []
    heapq.heappush(q, (0, start_x, start_y))
    distance[start_x][start_y] = 0

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

def solve():
    T = int(input())
    for tc in range(1, T+1):
        global N, graph, distance, dx, dy
        N = int(input())
        graph = [list(map(int, input())) for _ in range(N)]
        distance = [[INF] * N for _ in range(N)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        dijkstra(0, 0)
        print(f'#{tc} {distance[N-1][N-1]}')

if __name__ == '__main__':
    solve()