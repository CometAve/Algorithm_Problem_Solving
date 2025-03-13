# 문제 해결 방법
# 1. N개의 식재료를 N/2개씩 나누는 모든 경우의 수를 구한다.
# 2. 각각의 경우의 수에 대해 식재료들을 나누어 두 개의 요리를 만들어 맛의 차이를 계산한다.(절대값)
# 3. 맛의 차이가 최소인 경우를 찾아 출력한다.

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    # 최소 차이 값을 저장할 변수
    min_diff = 10000
    # 식재료들을 나누는 모든 경우의 수를 구한다.
    for i in range(1 << N): # 비트 연산을 사용하여 모든 경우의 수를 구한다.
        # A, B에 식재료들을 나누어 저장한다.
        A, B = [], []
        for j in range(N): # 식재료들을 나누어 저장한다.
            if i & (1 << j): # 비트 연산을 사용하여 식재료들을 나눈다.
                A.append(j)
            else:
                B.append(j)
        # 식재료들을 나누어 두 개의 요리를 만들어 맛의 차이를 계산한다.
        taste_A, taste_B = 0, 0 # A, B의 맛을 저장할 변수
        # A, B의 맛을 계산한다.
        for a in A:
            for b in A:
                taste_A += synergy[a][b] # A의 맛을 계산한다.
        for a in B:
            for b in B:
                taste_B += synergy[a][b] # B의 맛을 계산한다.
        # 맛의 차이가 최소인 경우를 찾아 저장한다.
        diff = abs(taste_A - taste_B) # 절대값 계산
        min_diff = min(min_diff, diff)
    print(f'#{tc} {min_diff}')