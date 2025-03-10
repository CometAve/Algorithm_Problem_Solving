T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list = [0] * 201
    for i in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        for j in range((a+1)//2, (b+1)//2+1):
            list[j] += 1
    print('#%d %d' % (tc, max(list)))