# a, b = map(int, input().split())
import sys

for line in sys.stdin:
    a, b = map(int, line.split())

    print(a + b)