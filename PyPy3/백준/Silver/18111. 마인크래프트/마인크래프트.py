import sys
input = sys.stdin.readline

# N: 세로, M: 가로, B: 인벤토리 속 블록 수
N, M, B = map(int, input().split())
# N x M 배열로 배치된 블록들 한 배열로 저장하려고 함
ground = []
for _ in range(N):
  ground.extend(map(int, input().split()))

min_time = 1e9
max_height = 0
max_ground = max(ground)
min_ground = min(ground)

for height in range(min_ground, max_ground+1):
    add = 0
    remove = 0
    now_time = 0
    for block in ground:
        if block > height:
            remove += block - height
        else:
            add += height - block
    now_time = remove * 2 + add
    if remove + B >= add:
      if now_time <= min_time:
          min_time = now_time
          max_height = height

print(min_time, max_height)