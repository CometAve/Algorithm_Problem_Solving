for _ in range(10):
    tc = int(input())
    password = list(map(int, input().split()))
    while password[-1] > 0:
        for i in range(1, 6):
            password.append(password.pop(0) - i)
            if password[-1] <= 0:
                password[-1] = 0
                break
    final_password = ' '.join(map(str, password))
    print(f'#{tc} {final_password}')