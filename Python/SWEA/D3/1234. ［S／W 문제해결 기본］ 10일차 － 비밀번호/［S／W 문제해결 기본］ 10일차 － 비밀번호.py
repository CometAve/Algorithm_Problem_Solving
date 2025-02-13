T = 10

def create_password(num_list):
    stack = []
    for num in num_list:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)
    return ''.join(stack)


for tc in range(1, T + 1):
    N, num_list = input().split()
    num_list = list(num_list)
    password = create_password(num_list)
    print(f'#{tc} {password}')