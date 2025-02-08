T = int(input())

for test_case in range(1, T + 1):
  # 주어진 숫자 개수
  N = int(input())
  
  # 숫자열 받기
  numbers = sorted(list(map(int, input().split())))
  
  print(f'#{test_case}', *numbers)