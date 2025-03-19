def solve():
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        parent = [i for i in range(N+1)]
        rank = [0] * (N+1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for _ in range(M):
            a, b = map(int, input().split())
            ra, rb = find(a), find(b)
            if ra == rb:
                continue
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        groups = set()
        for i in range(1, N+1):
            groups.add(find(i))
        print(f'#{tc} {len(groups)}')

if __name__ == '__main__':
    solve()