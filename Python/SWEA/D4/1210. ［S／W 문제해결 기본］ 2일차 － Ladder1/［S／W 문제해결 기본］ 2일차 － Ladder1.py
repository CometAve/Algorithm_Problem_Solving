for tc in range(1, 11):
  t = int(input())
  ladder = [list(map(int, input().split())) for _ in range(100)]

  # 도착점 찾기
  x = 99
  y = ladder[99].index(2)
  
  # 도착점에서 출발점 찾기
  while x > 0:
    # 위로 이동하면서 좌우 1 확인
    # 왼쪽에 1이 있는지 확인
    if y - 1 >= 0 and ladder[x][y - 1] == 1:
      # 좌로 이동하면서 위에 1이 있는지 확인
      while y - 1 >= 0 and ladder[x][y - 1] == 1:
        y -= 1
    # 오른쪽에 1이 있는지 확인
    elif y + 1 < 100 and ladder[x][y + 1] == 1:
      # 우로 이동하면서 위에 1이 있는지 확인
      while y + 1 < 100 and ladder[x][y + 1] == 1:
        y += 1
    
    # 위로 이동
    x -= 1
  print(f'#{tc} {y}')