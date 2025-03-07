T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    if M & ((1 << N) - 1) == (1 << N) - 1:
        result = 'ON'
    else:
        result = 'OFF'
    print(f'#{tc} {result}')