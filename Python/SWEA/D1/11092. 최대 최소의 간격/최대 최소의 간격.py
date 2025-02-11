T = int(input())
 
for test_case in range(1, T + 1):
  N = int(input())
  numbers = list(map(int, input().split()))
   
  # 문제 요구사항
  # 최소값이 여러 개일 경우 가장 작은 인덱스
  # 최대값이 여러 개일 경우 가장 큰 인덱스
  # 두 값의 차이를 구하여 절대값으로 출력하는 문제
   
  # 최대값과 최소값의 인덱스를 저장할 변수
  max_num_idx = 0
  min_num_idx = 0
   
  # 최소값 최댓값을 찾은 후 인덱스 저장
  for i in range(1, N):
    # 작다 비교 연산자를 통해 최소값의 가장 작은 인덱스만 저장
    if numbers[i] < numbers[min_num_idx]:
      min_num_idx = i
    # 크거나 같다 비교 연산자를 통해 최대값의 가장 마지막 인덱스를 저장
    if numbers[i] >= numbers[max_num_idx]:
      max_num_idx = i
       
  print(f'#{test_case} {abs(max_num_idx - min_num_idx)}')