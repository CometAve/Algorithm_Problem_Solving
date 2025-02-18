def evaluate_expression(expr):
    # 스택 초기화
    operand_stack = []
    operator_stack = []
    # 연산자 우선순위: 숫자가 높을수록 높은 우선순위
    precedence = {'+': 1, '*': 2}

    def apply_operator():
        op = operator_stack.pop()
        b = operand_stack.pop()
        a = operand_stack.pop()
        if op == '+':
            operand_stack.append(a + b)
        elif op == '*':
            operand_stack.append(a * b)
    
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch.isdigit():
            operand_stack.append(int(ch))
        elif ch in precedence:
            # 현재 연산자의 우선순위보다 우선순위가 높거나 같은 연산자가 operator_stack의 top에 있다면 계산 처리
            while operator_stack and precedence[ch] <= precedence[operator_stack[-1]]:
                apply_operator()
            operator_stack.append(ch)
        i += 1

    # 남은 연산자 처리
    while operator_stack:
        apply_operator()

    return operand_stack[0]

T = 10
for tc in range(1, T + 1):
    N = int(input())
    expr = input()
    result = evaluate_expression(expr)
    print(f'#{tc} {result}')
    