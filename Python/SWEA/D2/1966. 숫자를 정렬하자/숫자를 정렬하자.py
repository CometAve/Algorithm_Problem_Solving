T = int(input())

for test_case in range(1, T + 1):

  # 수의 개수 (5 <= N <= 50)
  N = int(input())
  
  # 입력받은 수를 저장할 리스트
  numbers = list(map(int, input().split()))

  # 카운트 배열 생성
  number_count = [0] * 51
  
  # 오름차순 정렬된 리스트
  sorted_list = []

  # 입력받은 수를 카운트 배열에 저장
  for number in numbers:
      number_count[number] += 1

  # 카운트 배열을 순회하면서
  # 0이 아닌 원소를 발견하면
  # 해당 인덱스를 그 원소의 개수만큼 sorted_list에 추가
  for i in range(0, 51):
      if number_count[i] != 0:
          for _ in range(number_count[i]):
              sorted_list.append(i)
  
  print(f'#{test_case} {" ".join(map(str, sorted_list))}')