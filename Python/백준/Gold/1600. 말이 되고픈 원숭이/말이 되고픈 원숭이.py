from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    K = int(input())
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    # 3차원 배열 - visited[x][y][z]:
    # x, y: 현재 위치, z: 지금까지 말처럼 이동한 횟수 (최대 K까지 가능)
    # 해당 위치에 도달했을 때 이동 횟수(시작점의 경우 1부터 기록)를 저장한다.
    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1  # 시작점 방문 체크
    
    # BFS를 위한 큐 초기화 : (x, y, 현재까지 사용한 말 이동 횟수)
    q = deque()
    q.append((0, 0, 0))
    
    # dx, dy 배열: 원숭이처럼 이동할 때 사용 (상하좌우)
    dx = [0, 0, 1, -1]  # 주석에서 8가지라고 되어있으나 실제 원숭이 이동은 4방향임.
    dy = [1, -1, 0, 0]
    
    # 말의 이동 방식: 8가지 방향
    horse_dx = [1, 2, 2, 1, -1, -2, -2, -1]
    horse_dy = [2, 1, -1, -2, -2, -1, 1, 2]
    
    while q:
        x, y, z = q.popleft()
        if x == N - 1 and y == M - 1:
            print(str(visited[x][y][z] - 1))
            return
        
        # 말처럼 이동 가능한 횟수가 남아 있다면 말 이동 시도를 함.
        if z < K:
            for i in range(8):
                nx, ny = x + horse_dx[i], y + horse_dy[i]
                # 경계 체크, 장애물(1) 체크, 방문 여부 체크
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and visited[nx][ny][z + 1] == 0:
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    q.append((nx, ny, z + 1))
        
        # 원숭이처럼 4방향 이동 (말 이동 사용 횟수 변경 없음)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
    
    print("-1")
    return

if __name__ == "__main__":
    solve()