def binary_search_competition(N, key):
    start = 1
    end = N
    count = 0
    
    if key == start or key == end:
        return 0
    else:
        while start <= end:
            middle = int((start + end) / 2)
            if middle == key:
                break
            elif middle > key:
                end = middle
                count += 1
            else:
                start = middle
                count += 1
    return count


T = int(input())

for test_case in range(1, T + 1):

    winner = ''

    N, a, b = map(int, input().split())

    a_count = binary_search_competition(N, a)
    b_count = binary_search_competition(N, b)

    if a_count < b_count:
        winner = "A"
    elif a_count == b_count:
        winner = "0"
    else:
        winner = "B"

    print(f'#{test_case} {winner}')