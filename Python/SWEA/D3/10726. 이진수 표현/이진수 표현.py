T = int(input())

result = []

for tc in range(1, T+1):
    N, M = map(int, input().split())
    if M % 2**N == 2**N - 1:
        result.append(f'#{tc} ON')
    else:
        result.append(f'#{tc} OFF')

print('\n'.join(result))