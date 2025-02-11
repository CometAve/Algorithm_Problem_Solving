T = int(input())
 
string = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 
for test_case in range(T):
     
    N, M = input().split()
    M = int(M)
    # '#' 제거
    N = N[1:]
    count_lst = [0] * 10
    numbers = input().split()
    # 외계어 숫자를 실제 숫자로 변환 인덱스 사용해서 카운팅 배열에 저장
    for number in numbers:
        count_lst[string.index(number)] += 1
        
    print(f'#{N}')
    for idx, value in enumerate(count_lst):
        print(f'{string[idx]} ' * value, end='')