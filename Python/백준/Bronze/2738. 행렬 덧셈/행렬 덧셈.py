import sys
input = sys.stdin.readline

# N * M 크기의 두 행렬 A, B를 더하는 프로그램

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# 행렬끼리 더한 값을 좌표에 맞게 저장할 이차원 배열 생성
sum_of_matrix = [[0] * M for _ in range(N)]

# 이차원 배열을 순회하면서
for i in range(N):
    for j in range(M):
        sum_of_matrix[i][j] = A[i][j] + B[i][j]

for sums in sum_of_matrix:
    print(*sums)