def can_place(x, y, dx, dy, board, n):
    path = []
    nx, ny = x + dx, y + dy
    while 0 <= nx < n and 0 <= ny < n:
        if board[nx][ny] != 0:
            return None
        path.append((nx, ny))
        nx += dx
        ny += dy
    return path

def dfs(idx, connected, total, cores, board, n, result):
    if len(cores) - idx + connected < result[0]:
        return
    if idx == len(cores):
        if connected > result[0] or (connected == result[0] and total < result[1]):
            result[0] = connected
            result[1] = total
        return
    x, y = cores[idx]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        path = can_place(x, y, dx, dy, board, n)
        if path is not None:
            for px, py in path:
                board[px][py] = 2
            dfs(idx + 1, connected + 1, total + len(path), cores, board, n, result)
            for px, py in path:
                board[px][py] = 0
    dfs(idx + 1, connected, total, cores, board, n, result)

def main():
    T = int(input())
    for tc in range(1, T + 1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        cores = []

        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                        continue
                    cores.append((i, j))

        result = [-1, float("inf")]
        dfs(0, 0, 0, cores, board, n, result)
        print(f"#{tc} {result[1]}")

if __name__ == '__main__':
    main()