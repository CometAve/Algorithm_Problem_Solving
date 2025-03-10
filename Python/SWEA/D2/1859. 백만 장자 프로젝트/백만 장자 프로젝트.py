T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 각 날의 매매가를 나타내는 자연수들 공백으로 구분됨
    prices = list(map(int, input().split()))  # 매매가 리스트
    max_profit = 0  # 최대 이익 초기화
    
    # 최대 이익을 구하기 위해 매매가 리스트를 뒤에서부터 순회
    # 뒤에서부터 순회하는 이유: 미래의 최대 가격을 기준으로 이익을 계산하기 위함
    prices = prices[::-1]  # 뒤에서부터 순회하기 위해 리스트를 뒤집음
    max_price = prices[0]  # 현재까지의 최대 매매가
    
    for i in range(1, N):
        if prices[i] < max_price:  # 현재 날짜의 매매가가 이후 최대 매매가보다 작다면
            max_profit += max_price - prices[i]  # 현재 가격에 구매해서 최대 가격에 판매
        else:  # 현재 날짜의 매매가가 최대 매매가보다 크다면
            max_price = prices[i]  # 최대 매매가 갱신

    print(f'#{tc} {max_profit}')