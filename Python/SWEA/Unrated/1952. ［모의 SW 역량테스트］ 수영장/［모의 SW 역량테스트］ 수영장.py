T = int(input())

for tc in range(1, T+1):
    # 1일, 1달, 3달, 1년 이용권의 금액
    day, month, three_month, year = map(int, input().split())
    # 각 달의 이용 계획
    plan = list(map(int, input().split()))
    # 1년 이용권을 사용하는 경우의 최소 비용을 저장할 변수
    min_cost = year
    # DP를 사용하여 최소 비용을 계산한다.
    dp = [0] * 12 # 12달의 최소 비용을 저장할 DP
    dp[0] = min(plan[0] * day, month) # 1일, 1달 이용권 중 최소 비용을 저장한다.
    dp[1] = dp[0] + min(plan[1] * day, month) # 1일, 1달 이용권 중 최소 비용을 저장한다.
    dp[2] = min(dp[1] + min(plan[2] * day, month), three_month) # 1일, 1달, 3달 이용권 중 최소 비용을 저장한다.
    for i in range(3, 12):
        dp[i] = min(dp[i-1] + min(plan[i] * day, month), dp[i-3] + three_month) # 1일, 1달, 3달 이용권 중 최소 비용을 저장한다.
    min_cost = min(min_cost, dp[-1]) # 1년 이용권을 사용하는 경우의 최소 비용을 저장한다.
    print(f'#{tc} {min_cost}')