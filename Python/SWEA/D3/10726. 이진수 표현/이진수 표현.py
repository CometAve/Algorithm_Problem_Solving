def dec_to_bin(n):
    if n == 0:
        return ""
    return dec_to_bin(n // 2) + str(n % 2)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = ''
    if dec_to_bin(M)[-N:] == '1'*N:
        result = 'ON'
    else:
        result = 'OFF'
    print(f'#{tc} {result}')