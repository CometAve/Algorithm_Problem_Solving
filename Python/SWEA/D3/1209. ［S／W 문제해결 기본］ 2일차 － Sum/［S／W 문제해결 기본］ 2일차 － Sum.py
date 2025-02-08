def get_max_sum(arr):
    """2차원 배열에서 행, 열, 대각선의 최대 합을 구하는 함수"""
    size = len(arr)
     
    # zip과 sum을 활용하여 각 행과 열의 합을 구함
    row_sums = [sum(row) for row in arr]  # 각 행의 합
    col_sums = [sum(col) for col in zip(*arr)]  # 각 열의 합
     
    # 대각선의 합을 구함
    diagonal1 = sum(arr[i][i] for i in range(size))  # 백슬래시
    diagonal2 = sum(arr[i][size-1-i] for i in range(size)) # 슬래시
     
    # 모든 합 중 최댓값을 반환
    return max(max(row_sums), max(col_sums), diagonal1, diagonal2)
 
 
for test_case in range(1, 11):
    # N : 테스트 케이스 번호
    N = int(input())
     
    # 2차원 배열 입력 받기
    arr = [list(map(int, input().split())) for _ in range(100)]
     
    result = get_max_sum(arr)
    print(f'#{N} {result}')