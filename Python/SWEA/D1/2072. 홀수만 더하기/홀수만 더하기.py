T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    sum_of_odd = 0
    for number in numbers:
        if number % 2 == 1:
            sum_of_odd += number
    print(f'#{tc} {sum_of_odd}')