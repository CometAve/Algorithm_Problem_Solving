for test_case in range(1, 11):
    N = int(input())
    b = list(map(int, input().split()))
    v = 0
    b_lst = []
    for i in range(2, N - 2):
        b_lst = [b[i-2], b[i-1], b[i],b[i+1], b[i+2]]
        b_lst.sort(reverse=True)
        if b[i] == b_lst[0]:
            v += b[i] - b_lst[1]
    print(f'#{test_case} {v}')