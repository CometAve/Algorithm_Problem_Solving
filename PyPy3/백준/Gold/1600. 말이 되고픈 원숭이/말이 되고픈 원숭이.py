from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    K = int(input())
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    # 방문 배열: 각 셀에서 도달 시 남은 말 이동 횟수의 최대값 저장
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = K
    
    # 큐에 상태 (x, y, 남은 말 이동 횟수, 이동 횟수) 저장
    q = deque([(0, 0, K, 0)])
    
    monkey_dx = [0, 0, 1, -1]
    monkey_dy = [1, -1, 0, 0]
    horse_dx = [1, 2, 2, 1, -1, -2, -2, -1]
    horse_dy = [2, 1, -1, -2, -2, -1, 1, 2]
    
    while q:
        x, y, remain, moves = q.popleft()
        
        if x == N - 1 and y == M - 1:
            print(str(moves))
            return
        
        # 원숭이처럼 4방향 이동
        for dx, dy in zip(monkey_dx, monkey_dy):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                # 이전에 더 많은 말 이동 가능 횟수를 가지고 방문한 적이 없다면 큐에 추가
                if visited[nx][ny] < remain:
                    visited[nx][ny] = remain
                    q.append((nx, ny, remain, moves + 1))
                    
        # 말 이동 (남은 횟수 > 0인 경우)
        if remain > 0:
            for dx, dy in zip(horse_dx, horse_dy):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                    if visited[nx][ny] < remain - 1:
                        visited[nx][ny] = remain - 1
                        q.append((nx, ny, remain - 1, moves + 1))
                        
    print("-1")

if __name__ == "__main__":
    solve()