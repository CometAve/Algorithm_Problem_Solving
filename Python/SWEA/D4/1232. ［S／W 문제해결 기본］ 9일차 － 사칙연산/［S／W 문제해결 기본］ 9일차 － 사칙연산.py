# 후위 순회로 계산
def calculate(node):
    if tree[node] not in '+-*/':  # 숫자면 바로 반환
        return float(tree[node])

    else:
        left_val = calculate(int(left[node]))
        right_val = calculate(int(right[node]))

        if tree[node] == '+':
            return left_val + right_val
        elif tree[node] == '-':
            return left_val - right_val
        elif tree[node] == '*':
            return left_val * right_val
        elif tree[node] == '/':
            return left_val / right_val
        else:
            return tree[node]

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(N):
        info = input().split()
        idx = int(info[0])

        if info[1] in '+-*/':  # 연산자인 경우
            tree[idx] = info[1]
            left[idx] = info[2]
            right[idx] = info[3]
        else:  # 숫자인 경우
            tree[idx] = info[1]

    result = int(calculate(1))
    print(f'#{tc} {result}')