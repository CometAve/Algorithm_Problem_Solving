from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

# bfs 탐색
def bfs():
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not tomatoes[nx][ny]:
                    tomatoes[nx][ny] = 1
                    queue.append((nx, ny))
    return days

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 익은 토마토의 위치를 찾아 큐에 넣는다.
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i, j))

# bfs 탐색
days = bfs()
# 모든 토마토가 익었는지 확인
for row in tomatoes:
    # 익지 않은 토마토가 있다면 -1 출력
    if 0 in row:
        print(str(-1))
        break
else:
    # 모든 토마토가 익었다면 익은 날짜 출력
    print(str(days))