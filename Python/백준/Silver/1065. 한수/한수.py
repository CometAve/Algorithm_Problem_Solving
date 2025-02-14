import sys
input = sys.stdin.readline

N = int(input())
sequence = 0

for i in range(1, N+1):
    if i < 100:
        sequence += 1
    else:
        num = list(map(int, str(i)))
        if num[0] - num[1] == num[1] - num[2]:
            sequence += 1

print(sequence)