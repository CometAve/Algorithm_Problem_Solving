import sys
input = sys.stdin.readline

def main():    
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    # dp[i]는 i원을 만들 수 있는 경우의 수
    dp = [0] * (k + 1)
    dp[0] = 1 # dp[0]은 1로 초기화 (0원을 만드는 방법은 아무것도 선택하지 않는 것)
    # 동전을 하나씩 확인하면서
    for coin in coins:
        # 동전의 가치부터 k원까지 dp 배열을 업데이트
        for i in range(coin, k + 1):
            # i원을 만들기 위해 coin을 사용하는 경우의 수는 dp[i - coin]과 같다
            dp[i] += dp[i - coin]
    print(dp[k])

if __name__ == "__main__":
    main()