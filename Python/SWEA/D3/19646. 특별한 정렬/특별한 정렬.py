T = int(input())
 
for test_case in range(1, T + 1):
 
    # N개의 정수
    N = int(input())
 
    # 정수 리스트
    count_list = [0] * 101
 
    # 입력과 동시에 카운팅 배열에 저장
    for i in input().split():
        count_list[int(i)] += 1
 
    # 카운팅 배열을 이용하여 내림차순으로 정렬된 리스트 생성
    numbers = []
    for i in range(100, 0, -1):
        numbers.extend([i] * count_list[i])
 
    # 한 개씩 번갈아가면서 출력
    for i in range(0, N, 2):
        numbers.insert(i+1, numbers.pop())
 
    result = ' '.join(map(str, numbers[:10]))
 
    print(f'#{test_case} {result}')