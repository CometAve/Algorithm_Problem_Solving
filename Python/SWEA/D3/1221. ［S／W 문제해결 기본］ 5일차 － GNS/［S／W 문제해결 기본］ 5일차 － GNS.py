T = int(input())

string_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

string_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(T):
    
    N, M = input().split()
    M = int(M)
    # '#' 제거
    N = N[1:]
    count_lst = [0] * 10

    for number in input().split():
        count_lst[string_dict[number]] += 1

    print(f'#{N}')
    # 한 단어를 하나씩 띄어서 출력하면서 한 줄로 출력
    for i in range(10):
        print(f'{string_lst[i]} ' * count_lst[i], end='')