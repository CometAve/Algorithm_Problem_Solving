# 지불할 돈 (1 <= M < 1000)
pay_money = int(input())

# 지폐 1000엔
bill = 1000

# 거스름돈
change = bill - pay_money

# 잔돈 개수
count_of_change = 0

# 잔돈 리스트
# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
change_list = [500, 100, 50, 10, 5, 1]

# 문제 요구사항
# 지불할 돈은 1 이상 1000미만이기 때문에
# 항상 1000엔 지폐 지불 고정
# 이때 잔돈 리스트를 보고
# 잔돈 개수를 가장 적게 주는 방법을 구하라.

# 내가 생각하는 풀이
# 지불할 돈을 잔돈 리스트의 원소들과
# 비교시키면서 원소보다
# 작으면 다음 원소와 비교하고 
# 크거나 같으면 몫을 구하여 잔돈 개수에 더함.
# 나머지를 그 다음 원소와 비교하여 반복
# 그리고 만약 나머지가 0일 경우 반복 종료

for i in change_list:
    if change == 0:
            break
    if change >= i:
        count_of_change += change // i
        change = change % i
    
print(count_of_change)
