for test_case in range(1, 11):
    N = int(input())
    b = list(map(int, input().split()))
    v = 0
    for i in range(2, N - 2):
        b_lst = b[i - 2:i + 3]
        c_b = b_lst.pop(2)
        highest = 0
        for h in b_lst:
            if h > highest:
                highest = h
        if c_b > highest:
            v += (c_b - highest)
    print(f'#{test_case} {v}')