T = int(input())

def get_max_flowers(i, j, N, M, balloons):
  x, y = i, j
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  current_flowers = balloons[i][j]
  total_flowers = current_flowers
  
  for i in range(4):
    for flower in range(1, current_flowers+1):
      nx, ny = x + dx[i] * flower, y + dy[i] * flower
      if 0 <= nx < N and 0 <= ny < M:
        total_flowers += balloons[nx][ny]
  return total_flowers

for test_case in range(1, T + 1):
  N, M = map(int, input().split())
  balloons = [list(map(int, input().split())) for _ in range(N)]
  sum_list = []
  max_sum = 0
  for i in range(N):
    for j in range(M):
      sum_list.append(get_max_flowers(i, j, N, M, balloons))
      
  for sum in sum_list:
    if sum > max_sum:
      max_sum = sum
  print(f'#{test_case} {max_sum}')