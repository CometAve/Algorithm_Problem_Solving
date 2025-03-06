T = int(input())

for tc in range(1, T+1):
    N, hexa = input().split()
    hexadecimal = '0123456789ABCDEF'
    result = ''
    for i in range(int(N)):
        for j in range(16):
            if hexa[i] == hexadecimal[j]:
                for k in range(3, -1, -1):
                    if 1 & (j >> k):
                        result += '1'
                    else:
                        result += '0'
    print(f'#{tc} {result}')