import sys
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    power = [0 for _ in range(N+1)]

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if x < y:
            parent[y] = x
            power[x] += power[y]
        else:
            parent[x] = y
            power[y] += power[x]

    for i in range(1, N+1):
        power[i] = int(input())

    for _ in range(M):
        O, P, Q = map(int, input().split())
        if O == 1:
            union(P, Q)
        else:
            P = find(P)
            Q = find(Q)
            if P == Q:
                power[P] = 0
            else:
                if power[P] > power[Q]:
                    power[P] -= power[Q]
                    power[Q] = 0
                    parent[Q] = P
                elif power[P] < power[Q]:
                    power[Q] -= power[P]
                    power[P] = 0
                    parent[P] = Q
                else:
                    power[P] = 0
                    power[Q] = 0

    answer = 0
    for i in range(1, N+1):
        if find(i) == i and power[i] != 0:
            answer += 1

    print(str(answer) + '\n')
    survivors = []
    for i in range(1, N+1):
        if find(i) == i and power[i] != 0:
            survivors.append(power[i])
    survivors.sort()
    for i in survivors:
        print(str(i) + ' ')

if __name__ == '__main__':
    solve()