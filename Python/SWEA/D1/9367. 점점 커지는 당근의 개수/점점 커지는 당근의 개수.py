T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_length = 1
    current_length = 1
    for i in range(1, N):
        if arr[i] > arr[i - 1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1
        
    print(f'#{tc} {max_length}')
