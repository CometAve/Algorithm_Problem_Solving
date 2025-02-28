T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_start(r, c):
    up_r = r + dr[0]
    up_c = c + dc[0]
    if up_r >= 0 and graph[up_r][up_c] == 1:
        return False

    left_r = r + dr[2]
    left_c = c + dc[2]
    if left_c >= 0 and graph[left_r][left_c] == 1:
        return False

    return True


def calc_area(r, c):
    width = height = 0

    wr = r
    wc = c
    while wc < N:
        if graph[wr][wc] != 1:
            break
        width += 1
        wr += dr[3]
        wc += dc[3]

    hr = r
    hc = c
    while hr < N:
        if graph[hr][hc] != 1:
            break
        height += 1
        hr += dr[1]
        hc += dc[1]

    return width * height


for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_area = float('-inf')

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and is_start(i, j):
                max_area = max(max_area, calc_area(i, j))

    print(f'#{tc} {max_area}')