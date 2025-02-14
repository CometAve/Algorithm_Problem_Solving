import sys
input = sys.stdin.readline

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

N = int(input())

# 작은 경우 별도 처리
if N <= 2:
    print(2)
    sys.exit(0)
if N <= 3:
    print(3)
    sys.exit(0)
if N <= 5:
    print(5)
    sys.exit(0)
if N <= 7:
    print(7)
    sys.exit(0)
if N <= 11:
    print(11)
    sys.exit(0)

# N이 짝수면 다음 홀수부터 시작
i = N
if i % 2 == 0:
    i += 1

while True:
    if is_palindrome(i) and is_prime(i):
        print(i)
        break
    i += 2  # 짝수는 건너