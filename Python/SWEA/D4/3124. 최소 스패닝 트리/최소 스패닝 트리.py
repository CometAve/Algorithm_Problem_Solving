def find_parent(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    
    edges.sort(key=lambda x: x[0])
    parents = [i for i in range(v + 1)]
    
    cnt = 0
    result = 0
    for cost, a, b in edges:
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            result += cost
            cnt += 1
        if cnt == v - 1:
            break

    print(f'#{tc} {result}')