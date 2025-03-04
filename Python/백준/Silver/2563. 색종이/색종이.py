# 색종이 개수 입력
n = int(input())

# 도화지를 100×100 2차원 배열로 초기화 (0: 미표시, 1: 색종이로 덮인 칸)
canvas = [[0] * 100 for _ in range(100)]

for _ in range(n):
    # 왼쪽 아래 좌표 (x, y)를 입력받음 (문제에 따라 좌표 기준이 다를 수 있음)
    x, y = map(int, input().split())
    # 색종이는 10×10 크기이므로, x ~ x+9, y ~ y+9 범위를 덮음
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1  # 이미 덮인 칸은 덮어써도 1 그대로

# 전체 도화지에서 1인 칸(색종이가 덮인 칸)의 수를 계산
area = sum(sum(row) for row in canvas)
print(area)
