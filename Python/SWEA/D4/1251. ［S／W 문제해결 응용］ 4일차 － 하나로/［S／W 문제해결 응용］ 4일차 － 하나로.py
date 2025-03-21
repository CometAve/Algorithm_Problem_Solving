# 크루스칼 알고리즘을 사용한 풀이
def solve():
    T = int(input())

    for tc in range(1, T+1):
        n = int(input())
        x_coord = list(map(int, input().split()))
        y_coord = list(map(int, input().split()))
        tax = float(input())

        edges = []
        for i in range(n):
            for j in range(i+1, n):
                edges.append((i, j, (x_coord[i] - x_coord[j])**2 + (y_coord[i] - y_coord[j])**2))

        edges.sort(key=lambda x: x[2])

        p = [i for i in range(n)]
        rank = [0] * n

        def find_set(x):
            if p[x] != x:
                p[x] = find_set(p[x])
            return p[x]

        def union(x, y):
            px = find_set(x)
            py = find_set(y)

            if rank[px] > rank[py]:
                p[py] = px
            else:
                p[px] = py
                if rank[px] == rank[py]:
                    rank[py] += 1

        result = 0
        for u, v, w in edges:
            if find_set(u) != find_set(v):
                union(u, v)
                result += w

        print(f'#{tc} {round(result * tax)}')

if __name__ == '__main__':
    solve()