import sys
input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
r, c = 0, 0
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max_num:
            max_num = matrix[i][j]
            r, c = i + 1, j + 1

print(f'{max_num}\n{r} {c}')