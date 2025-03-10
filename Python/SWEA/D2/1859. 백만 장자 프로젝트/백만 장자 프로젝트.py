T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    max_profit = 0
    
    # 배열을 뒤집지 않고 뒤에서부터 순회
    max_price = prices[-1]
    
    for i in range(N-2, -1, -1):  # 뒤에서 두 번째부터 처음까지 역순으로
        if prices[i] < max_price:
            max_profit += max_price - prices[i]
        else:
            max_price = prices[i]

    print(f'#{tc} {max_profit}')