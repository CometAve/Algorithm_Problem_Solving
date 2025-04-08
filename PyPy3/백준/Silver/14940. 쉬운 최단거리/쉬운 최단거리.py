# 쉬운 최단거리
# https://www.acmicpc.net/problem/14940
# 1. 2 : 목표 지점, 1 : 길, 0 : 벽
# 2. 2 : 단 한개
# 3. 지도가 주어지면 각 지점에서 목표 지점까지의 최단 거리를 구하여 기록
# 4. 만약 목표 지점에 도달할 수 없는 경우 -1을 기록
# 5. BFS를 사용하여 최단 거리 구하기

import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, n, m, graph):
    queue = deque([start])
    visited = [[-1] * m for _ in range(n)]
    visited[start[0]][start[1]] = 0
    
    # 벽(0)인 위치는 시작부터 0으로 초기화
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                visited[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 방문 가능한 위치 확인 (벽이 아닌 곳)
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return visited

def solve():
    n, m = map(int, input().split())
    graph = []
    target = None
    
    # 입력과 동시에 목표 지점 찾기
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
        if not target:
            for j in range(m):
                if row[j] == 2:
                    target = (i, j)
    
    # BFS 수행
    visited = bfs(target, n, m, graph)
    
    # 결과 출력 (join으로 최적화)
    for i in range(n):
        print(" ".join(map(str, visited[i])))
        if i < n-1:
            print("\n")

if __name__ == "__main__":
    solve()