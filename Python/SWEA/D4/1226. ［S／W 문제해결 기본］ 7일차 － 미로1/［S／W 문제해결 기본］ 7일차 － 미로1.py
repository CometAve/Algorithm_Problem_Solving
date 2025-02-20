def find_path(x, y, N):
    visited = [[0] * N for _ in range(N)]
    queue = [[x, y]]
    visited[x][y] = 1

    while queue:
        exx, exy = queue.pop(0)
        if maze[exx][exy] == 3:
            return 1
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            adjx, adjy = exx + dx, exy + dy
            if 0 <= adjx < N and 0 <= adjy < N and maze[adjx][adjy] != 1 and visited[adjx][adjy] == 0:
                queue.append([adjx, adjy])
                visited[adjx][adjy] = visited[exx][exy] + 1

    return 0


for _ in range(10):
    tc = int(input())
    N = 16
    maze = [list(map(int, input().strip())) for _ in range(N)]
    stx, sty = 1, 1
    ans = find_path(stx, sty, N)
    print(f'#{tc} {ans}')
