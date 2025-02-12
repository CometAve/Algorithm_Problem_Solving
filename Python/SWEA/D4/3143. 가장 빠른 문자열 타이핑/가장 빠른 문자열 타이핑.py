T = int(input())

for tc in range(1, T + 1):
    A, B = map(str, input().split())
    count = A.count(B)
    print(f'#{tc} {len(A)-(len(B) * count) + count}')