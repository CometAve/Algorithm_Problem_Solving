T = int(input())

for test_case in range(1, T + 1):
  # 수열의 길이
  N = int(input())
  
  # 입력 수열 0으로 split하여 가장 긴 '1'의 연속 횟수를 구한다.
  max_count = max(map(len, input().split('0')))
  
  print(f'#{test_case} {max_count}')