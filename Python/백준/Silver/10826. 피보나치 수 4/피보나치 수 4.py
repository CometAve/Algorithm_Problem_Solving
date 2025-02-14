import sys
input = sys.stdin.readline

def fibonacci(n):
  if n < 2:
    return n
  dp = [0] * (n + 1)
  dp[0], dp[1] = 0, 1
  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  return dp[n]

n = int(input().strip())
print(fibonacci(n))