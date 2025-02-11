T = int(input())

def get_candidate_landing_spots(N, M, arr):
    candidate_spots = 0
    for i in range(N):
        for j in range(M):
            current_height = arr[i][j]
            possible = 0

            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] < current_height:
                    possible += 1
                    if possible == 4:
                        candidate_spots += 1
                        break

    return candidate_spots
        

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num_of_spots = get_candidate_landing_spots(N, M, arr)

    print(f'#{tc} {num_of_spots}')