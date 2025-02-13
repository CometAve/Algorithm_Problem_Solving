T = int(input())

for tc in range(1, T+1):
  # N: 숫자열 A의 길이, M: 숫자열 B의 길이
  N, M = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  max_multiplication = -200 # 문제 조건 고려

  if N < M:
    N, M = M, N
    A, B = B, A


  for i in range(N-M+1): # 긴 배열에서 기준 위치
    temp = 0            # 기준위치부터 마주보는 원소들의 곱의 합
    for j in range(M): # 짧은 배열에서 비교하는 위치
      temp += A[i+j] * B[j]
    if temp > max_multiplication:
      max_multiplication = temp
  
    
  print(f'#{tc} {max_multiplication}')