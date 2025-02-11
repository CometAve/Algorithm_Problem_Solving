T = int(input())
 
num_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
str_dict = {num: idx for idx, num in enumerate(num_lst)}

for test_case in range(1, T+1):
     
    N, M = input().split()
    count_lst = [0] * 10
    
    for number in input().split():
        count_lst[str_dict[number]] += 1
 
    print(f'#{test_case}')
    for idx, count in enumerate(count_lst):
        print((f'{num_lst[idx]} ' * count), end='')