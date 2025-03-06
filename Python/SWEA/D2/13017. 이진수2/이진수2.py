T = int(input())

for tc in range(1, T+1):
    N = float(input())
    result = ''
    for i in range(1, 13):
        # N이 2**(-i)보다 크면 1을 추가하고 N에서 2**(-i)를 뺀다
        # 예를 들어, N이 0.625이면
        # i가 1일 때, 2**(-i)는 0.5이므로 N이 0.5보다 크므로 1을 추가하고 N에서 0.5를 뺀다
        if N >= 2**(-i):
            N -= 2**(-i) # N = 0.125
            result += '1'
        # i가 2일 때, 2**(-i)는 0.25이므로 N이 0.125보다 작으므로 0을 추가한다
        else:
            result += '0'
        if N == 0:
            break
    # 13자리 이상이면 overflow
    else:
        result = 'overflow'
    print(f'#{tc} {result}')