import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

N = int(input())

for i in range(N, 1003002):
    s = str(i)
    # 회문이 아니면 소수검사 안함
    if s != s[::-1]:
        continue
    if is_prime(i):
        print(i)
        break