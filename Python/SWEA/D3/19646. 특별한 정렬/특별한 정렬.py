T = int(input())
 
for test_case in range(1, T + 1):
 
    # N개의 정수
    N = int(input())
 
    # 정수 리스트
    numbers = list(map(int, input().split()))
 
    # 내림차순 정렬
    numbers.sort(reverse=True)
 
    # 한 개씩 번갈아가면서 출력
    for i in range(0, N, 2):
        numbers.insert(i+1, numbers.pop())
 
    result = ' '.join(map(str, numbers[:10]))
 
    print(f'#{test_case} {result}')
