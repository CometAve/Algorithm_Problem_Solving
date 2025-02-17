T = 10

for tc in range(1, T+1):
  N = int(input())
  formula = list(map(int, input().split('+')))
  print(f'#{tc} {sum(formula)}')