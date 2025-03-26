import sys
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    N = int(input())
    M = int(input())
    parent = [i for i in range(N+1)]

    def find_parent(x):
        if parent[x] == x:
            return x
        parent[x] = find_parent(parent[x])
        return parent[x]

    # 두 노드를 연결
    def union(x, y):
        x = find_parent(x)
        y = find_parent(y)
        # 더 작은 노드를 부모로 설정
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()
    result = 0
    for edge in edges:
        c, a, b = edge
        if find_parent(a) != find_parent(b):
            union(a, b)
            result += c
    
    print(str(result))


if __name__ == "__main__":
    solve()