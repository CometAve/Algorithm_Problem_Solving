T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        for x in range(1, j+1):
            if i-x-1 >= 0 and i+x-1 < len(stones) and stones[i-x-1] == stones[i+x-1]:
                stones[i-x-1] = (stones[i-x-1]+1) % 2
                stones[i+x-1] = (stones[i+x-1]+1) % 2

    print(f'#{tc}', *stones)