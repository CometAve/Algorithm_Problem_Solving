import sys
input = sys.stdin.readline
print = sys.stdout.write

def find_parent(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    # rank
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solve():
    N = int(input())
    M = int(input())
    parent = [i for i in range(N+1)]
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])
    result = 0
    for edge in edges:
        a, b, c = edge
        if find_parent(a, parent) != find_parent(b, parent):
            union(a, b, parent)
            result += c
    
    print(str(result))

if __name__ == "__main__":
    solve()