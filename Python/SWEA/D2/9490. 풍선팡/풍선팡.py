def boom():
    mx = 0
    dirs = ((1,0), (-1,0), (0,1), (0,-1))
    
    for i in range(N):
        for j in range(M):
            power = arr[i][j]
            current = power
            
            # 방향별로 한번에 계산
            for dy, dx in dirs:
                for p in range(1, power + 1):
                    ny, nx = i + dy * p, j + dx * p
                    if 0 <= ny < N and 0 <= nx < M:
                        current += arr[ny][nx]
            
            mx = max(mx, current)
    return mx

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case} {boom()}')