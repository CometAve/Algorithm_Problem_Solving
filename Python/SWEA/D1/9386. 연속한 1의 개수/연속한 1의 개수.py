T = int(input())
 
for test_case in range(1, T + 1):
  N = int(input())

  max_count = max(map(len, input().split('0')))
   
  print(f'#{test_case} {max_count}')