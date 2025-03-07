def solution():
    target = M
    for _ in range(N):
        if target & 1 == 0:
            return "OFF"
        target >>= 1
    return "ON"

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {solution()}')