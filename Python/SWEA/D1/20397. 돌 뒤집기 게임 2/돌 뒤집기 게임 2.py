T = int(input())
            
for tc in range(1, T+1):
    # N: 돌의 개수, M: 뒤집기 횟수
    N, M = map(int, input().split())

    # 돌의 초기 상태
    stones = list(map(int, input().split()))

    for _ in range(M):
        # i번째 돌을 사이에 두고 마주보는 j개의 돌의 색을 확인 후 뒤집는다.
        i, j = map(int, input().split())
        i -= 1 # i번째 돌 -> i-1 인덱스
        for k in range(1, j+1): # k i번째 돌에서의 거리
            if 0 <= i-k and i+k < N:
                # 같은 색이면 뒤집고, 다른 색이면 그대로
                if stones[i-k] == stones[i+k]:
                    # if stones[i-k]:   # if stones[i-k] == 1:
                    #     stones[i-k] = 0
                    #     stones[i+k] = 0
                    # else:             # stones[i-k] == 0
                    #     stones[i-k] = 1
                    #     stones[i+k] = 1
                    stones[i-k] = (stones[i-k]+1)%2  # stones[i-k] ^= 1
                    stones[i+k] = (stones[i+k]+1)%2
    
    print(f'#{tc}', *stones)