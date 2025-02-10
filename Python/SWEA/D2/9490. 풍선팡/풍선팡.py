T = int(input())

def get_max_flowers(i, j, N, M, balloons):
  power = balloons[i][j]
  total = power
  
  for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
    for dist in range(1, power+1):
      ni, nj = i + di * dist, j + dj * dist
      if 0 <= ni < N and 0 <= nj < M:
        total += balloons[ni][nj]
  return total 

for test_case in range(1, T + 1):
  N, M = map(int, input().split())
  balloons = [list(map(int, input().split())) for _ in range(N)]
  max_sum = 0
  for i in range(N):
    for j in range(M):
      max_sum = max(max_sum, get_max_flowers(i, j, N, M, balloons))
      
  print(f'#{test_case} {max_sum}')