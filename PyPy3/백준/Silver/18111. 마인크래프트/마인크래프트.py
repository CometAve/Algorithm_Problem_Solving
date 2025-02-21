import sys
input = sys.stdin.readline

# N: 세로, M: 가로, B: 인벤토리 속 블록 수
N, M, B = map(int, input().split())
# N x M 배열로 배치된 블록들
blocks = [list(map(int, input().split())) for _ in range(N)]

min_time = 1e9
max_height = 0
for h in range(257):
    time = 0
    block = B
    for i in range(N):
        for j in range(M):
            if blocks[i][j] < h:
                time += h - blocks[i][j]
                block -= h - blocks[i][j]
            else:
                time += 2 * (blocks[i][j] - h)
                block += blocks[i][j] - h
    if block < 0:
        continue
    if time <= min_time:
        min_time = time
        max_height = h

print(min_time, max_height)