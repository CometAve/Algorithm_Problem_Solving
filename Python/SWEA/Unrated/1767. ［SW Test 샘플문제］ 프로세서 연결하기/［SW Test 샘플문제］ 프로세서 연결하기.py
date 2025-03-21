# 설계
# 1. 가장자리에 있는 코어는 이미 전원이 연결된 것으로 간주한다.
# 2. 코어를 연결할 수 있는 방향은 상하좌우 4방향이다.
# 3. 코어를 연결할 수 있는지 확인하는 함수를 만든다.
# 4. dfs로 코어를 연결할지 말지 결정한다.
# 5. dfs(idx, connected, total, cores, board, n, result)
# 6. idx: 현재 코어 인덱스, connected: 연결된 코어 수, total: 전선 길이, cores: 코어 위치, board: 멕시노스, n: 멕시노스 크기, result: [최대로 연결된 코어의 수, 최소 전선 길이]
# 7. dfs 종료 조건: idx == len(cores) 
# 8. result 업데이트

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
    if idx == len(cores):
        if connected > result[0] or (connected == result[0] and total < result[1]):
            result[0] = connected
            result[1] = total
        return

    x, y = cores[idx]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        path = can_place(x, y, dx, dy, board, n)
        if path is not None:
            # 전선 설치
            for px, py in path:
                board[px][py] = 2
            dfs(idx + 1, connected + 1, total + len(path), cores, board, n, result)
            # 복구
            for px, py in path:
                board[px][py] = 0
    # 해당 코어를 연결하지 않는 경우
    dfs(idx + 1, connected, total, cores, board, n, result)

def main():
    T = int(input())
    for tc in range(1, T + 1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]

        cores = []
        for i in range(n):
            for j in range(n):
                # 가장자리에 있지 않은 코어만 선택
                if board[i][j] == 1:
                    if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                        continue
                    cores.append((i, j))

        # result: [최대로 연결된 코어의 수, 최소 전선 길이]
        result = [-1, float("inf")]
        dfs(0, 0, 0, cores, board, n, result)
        print(f"#{tc} {result[1]}")

if __name__ == '__main__':
    main()