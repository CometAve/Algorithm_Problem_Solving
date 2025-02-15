T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    balloons = [list(map(int, input().split())) for _ in range(N)]
    max_sum = float('-inf')
    min_sum = float('inf')
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            current_sum = balloons[i][j]
            for n in range(4):
                for k in range(1, N):
                    ni = i + di[n] * k
                    nj = j + dj[n] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        current_sum += balloons[ni][nj]
            
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < min_sum:
                min_sum = current_sum

    print(f'#{tc} {max_sum - min_sum}')