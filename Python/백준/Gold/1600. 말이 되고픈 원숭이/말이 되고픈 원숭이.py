from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    K = int(input())
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    visited = set()
    visited.add((0, 0, 0))
    
    monkey_q = deque([(0, 0, 0)])
    horse_q = deque([])
    
    monkey_dx = [0, 0, 1, -1]
    monkey_dy = [1, -1, 0, 0]
    horse_dx = [1, 2, 2, 1, -1, -2, -2, -1]
    horse_dy = [2, 1, -1, -2, -2, -1, 1, 2]
    
    moves = 0
    while monkey_q or horse_q:
        next_monkey = deque()
        next_horse = deque()
        
        while monkey_q:
            x, y, horse_used = monkey_q.popleft()
            if x == N - 1 and y == M - 1: 
                print(str(moves))
                return
            for dx, dy in zip(monkey_dx, monkey_dy):
                nx, ny = x + dx, y + dy
                state = (nx, ny, horse_used)
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and state not in visited:
                    visited.add(state)
                    next_monkey.append(state)
            if horse_used < K:
                for dx, dy in zip(horse_dx, horse_dy):
                    nx, ny = x + dx, y + dy
                    state = (nx, ny, horse_used + 1)
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and state not in visited:
                        visited.add(state)
                        next_horse.append(state)
        
        while horse_q:
            x, y, horse_used = horse_q.popleft()
            if x == N - 1 and y == M - 1:
                print(str(moves))
                return
            for dx, dy in zip(monkey_dx, monkey_dy):
                nx, ny = x + dx, y + dy
                state = (nx, ny, horse_used)
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and state not in visited:
                    visited.add(state)
                    next_monkey.append(state)
            if horse_used < K:
                for dx, dy in zip(horse_dx, horse_dy):
                    nx, ny = x + dx, y + dy
                    state = (nx, ny, horse_used + 1)
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and state not in visited:
                        visited.add(state)
                        next_horse.append(state)
                        
        moves += 1
        monkey_q = next_monkey
        horse_q = next_horse

    print("-1")

if __name__ == "__main__":
    solve()