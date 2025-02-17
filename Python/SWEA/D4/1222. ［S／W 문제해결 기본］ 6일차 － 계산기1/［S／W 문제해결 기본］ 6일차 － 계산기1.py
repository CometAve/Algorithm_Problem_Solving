T = 10

# 중위표기식 -> 후위표기식
for tc in range(1, T+1):
  N = int(input())
  formula = input()
  stack = []
  operator_stack = []
  calculator = []
  result = 0
    
  for i in range(N):
    if formula[i].isdigit():
      stack.append(formula[i])
    elif formula[i] == '+':
      operator_stack.append(formula[i])
  else:
    while operator_stack:
      stack.append(operator_stack.pop())
    
    for i in range(N):
      if stack[i].isdigit():
        calculator.append(int(stack[i]))
      elif stack[i] == '+':
        if len(calculator) >= 2:
          a = calculator.pop()
          b = calculator.pop()
          calculator.append(a + b)
    result = calculator[0]  
  print(f'#{tc} {result}')