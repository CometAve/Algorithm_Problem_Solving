T = int(input())
 
string_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
 
string_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 
for test_case in range(T):
     
    N, M = input().split()
    M = int(M)
    # '#' 제거
    N = N[1:]
    count_lst = [0] * 10
    numbers = input().split()
    # 외계어 숫자를 실제 숫자로 변환하여 카운트
    for number in numbers:
        count_lst[string_dict[number]] += 1
 
    print(f'#{N}')
    for idx, value in enumerate(count_lst):
        print(f'{string_lst[idx]} ' * value, end="")