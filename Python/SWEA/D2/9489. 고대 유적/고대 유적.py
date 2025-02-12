T = int(input())

for tc in range(1, T+1):
  N, M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]

  max_length = 0
  count = 0

  for i in range(N):
    count = 0
    for j in range(M):
      if arr[i][j] == 1:
        count += 1
        if count > max_length:
          max_length = count
      else:
        count = 0
  
  for j in range(M):
    count = 0
    for i in range(N):
      if arr[i][j] == 1:
        count += 1
        if count > max_length:
          max_length = count
      else:
        count = 0
  print(f'#{tc} {max_length}')