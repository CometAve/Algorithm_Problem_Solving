import sys
input = sys.stdin.readline

# N: 세로, M: 가로, B: 인벤토리 속 블록 수
N, M, B = map(int, input().split())
# 높이 카운팅 정렬 배열 생성
heights = [0] * 257
# 최소 시간, 최대 높이
min_time, max_height = 1e9, 0
# 땅 높이 가져오면서 높이별 카운팅
for _ in range(N):
    for h in map(int, input().split()):
        heights[h] += 1

# 블록을 놓을 높이를 256까지 순회
for target_height in range(257):
    # 블록을 놓을 높이가 target_height일 때의 시간
    time = 0
    # 인벤토리 속 블록 수
    blocks = B
    # 각 높이별로 순회
    for height, count in enumerate(heights):
        # 높이가 target_height보다 낮은 경우
        if height < target_height:
            # 블록을 쌓아야 하는 높이만큼 블록을 인벤토리에서 꺼냄
            blocks -= (target_height - height) * count
            # 시간은 블록을 쌓아야 하는 높이만큼 블록을 꺼내는 시간
            time += (target_height - height) * count
        # 높이가 target_height보다 높은 경우
        elif height > target_height:
            # 블록을 쌓아야 하는 높이만큼 블록을 인벤토리에 넣음
            blocks += (height - target_height) * count
            # 시간은 블록을 쌓아야 하는 높이만큼 블록을 넣는 시간
            time += 2 * (height - target_height) * count

    # 인벤토리 속 블록 수가 음수가 아니면
    if blocks >= 0:
        # 시간이 최소 시간보다 작으면
        if time <= min_time:
            # 최소 시간 갱신
            min_time = time
            # 최대 높이 갱신
            max_height = target_height
            
print(min_time, max_height)