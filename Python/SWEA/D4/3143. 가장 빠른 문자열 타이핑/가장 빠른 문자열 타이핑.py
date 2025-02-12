T = int(input())

for tc in range(1, T + 1):
    A, B = map(str, input().split())
    N = len(A)
    M = len(B)
    cnt = 0
    i = 0
    while i < N:
        if A[i:i+M] == B:
            cnt += 1
            i += M
        else:
            i += 1
    print(f'#{tc} {N - cnt * (M - 1)}')