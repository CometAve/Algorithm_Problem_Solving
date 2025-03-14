def subset(idx, sum):
    global cnt
    if sum > K:
        return
    if idx == N:
        if sum == K:
            cnt += 1
        return
    subset(idx+1, sum+sequence[idx])
    subset(idx+1, sum)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))

    cnt = 0
    
    subset(0, 0)

    print(f'#{tc} {cnt}')