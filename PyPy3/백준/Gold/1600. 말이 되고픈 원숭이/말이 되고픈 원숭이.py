from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    K = int(input())
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    # (x, y, 말 이동 사용 횟수)
    visited = set()
    visited.add((0, 0, 0))
    
    # (x, y, 말 이동 사용 횟수, 현재까지 이동 횟수)
    q = deque([(0, 0, 0, 0)])
    
    monkey_dx = [0, 0, 1, -1]
    monkey_dy = [1, -1, 0, 0]
    
    horse_dx = [1, 2, 2, 1, -1, -2, -2, -1]
    horse_dy = [2, 1, -1, -2, -2, -1, 1, 2]
    
    while q:
        x, y, horse_used, moves = q.popleft()
        
        if x == N - 1 and y == M - 1:
            print(str(moves))
            return
        
        # 말 이동 사용 수는 그대로 유지
        for dx, dy in zip(monkey_dx, monkey_dy):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                state = (nx, ny, horse_used)
                if state not in visited:
                    visited.add(state)
                    q.append((nx, ny, horse_used, moves + 1))
        
        # 말 이동 사용 수 1 증가 (단, K 이내)
        if horse_used < K:
            for dx, dy in zip(horse_dx, horse_dy):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                    state = (nx, ny, horse_used + 1)
                    if state not in visited:
                        visited.add(state)
                        q.append((nx, ny, horse_used + 1, moves + 1))
    
    print("-1")

if __name__ == "__main__":
    solve()