T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    if M % (2**N) == 2**N - 1:
        result.append('ON')
    else:
        result.append('OFF')
    print(f'#{tc} {result[0]}')