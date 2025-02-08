	
for test_case in range(1, 11):
  # N : 테스트 케이스 번호
  N = int(input())
   
  # 문제분석
  # 100x100 크기의 2차원 배열이 주어질 때,
  # 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 문제
  # 배열의 크기는 100x100으로 고정
   
  # 2차원 배열을 입력 받기
  arr = [list(map(int, input().split())) for _ in range(100)]
  # 합 중 최댓값을 저장할 변수
  max_sum = 0
   
  # 각 행의 합들을 저장할 리스트
  row_sum = [0] * 100
  # 행의 합들 중 최댓값을 저장할 변수
  max_row_sum = 0
   
  # 각 열의 합들을 저장할 리스트
  column_sum = [0] * 100
  # 열의 합들 중 최댓값을 저장할 변수
  max_column_sum = 0
   
  # 각 행의 합을 구하여 리스트 row_sum에 저장
  for i in range(100):
    for j in range(100):
      row_sum[i] += arr[i][j]
    # 행의 합 중 최댓값을 구하여 max_row_sum에 저장
    if row_sum[i] > max_row_sum:
      max_row_sum = row_sum[i]
     
  # 각 열의 합을 구하여 리스트 col_sum에 저장
  for j in range(100):
    for i in range(100):
      column_sum[j] += arr[i][j]
    # 열의 합 중 최댓값을 구하여 max_column_sum에 저장
    if column_sum[j] > max_column_sum:
      max_column_sum = column_sum[j]
 
  # 각 대각선의 합을 구하기 위한 변수
  primary_diagonal_sum = 0
  secondary_diagonal_sum = 0
 
  # 백슬래쉬 대각선
  for i in range(100):
    primary_diagonal_sum += arr[i][i]
 
  # 슬래쉬 대각선
  for i in range(100):
    secondary_diagonal_sum += arr[i][100-1-i]
   
  sum_list = [max_row_sum, max_column_sum, primary_diagonal_sum, secondary_diagonal_sum]
  # 행의 합 최댓값, 열의 합 최댓값, 대각선의 합 중 최댓값을 구하여 max_sum에 저장
  for i in sum_list:
    if i > max_sum:
      max_sum = i
  print(f'#{N} {max_sum}')