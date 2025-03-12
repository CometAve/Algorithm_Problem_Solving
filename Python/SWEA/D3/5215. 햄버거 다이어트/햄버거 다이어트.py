T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    score = [0] * N
    cal = [0] * N
    for i in range(N):
        score[i], cal[i] = map(int, input().split())
    # max_score[i][j] : i번째 재료까지 사용해서 칼로리가 j일 때 얻을 수 있는 최대 점수 저장
    max_score = [[0] * (L+1) for _ in range(N+1)]
    # max_score[i][j]: i번째 재료까지 고려했을 때, 총 칼로리가 j 이하인 조합에서 얻을 수 있는 최대 맛 점수

    # 각 재료에 대해 선택 여부 결정
    for i in range(1, N+1):
        for j in range(1, L+1):
            # 현재 재료(i-1)를 선택할 수 있는 경우(칼로리 제한을 넘지 않는 경우)
            if cal[i-1] <= j:
                # 두 경우 중 최댓값 선택:
                # 1) i번째 재료를 선택하는 경우: 이전 재료까지의 j-cal[i-1] 제한에서의 최적 + 현재 재료 점수
                # 2) i번째 재료를 선택하지 않는 경우: 이전 재료까지의 j 제한에서의 최적
                max_score[i][j] = max(max_score[i-1][j], max_score[i-1][j-cal[i-1]] + score[i-1])
            else:
                # 현재 재료의 칼로리가 제한을 초과하면 이전 단계의 결과 그대로 사용
                max_score[i][j] = max_score[i-1][j]
    print(f'#{tc} {max_score[N][L]}')