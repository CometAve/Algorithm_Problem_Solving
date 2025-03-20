import sys
input = sys.stdin.readline
print = sys.stdout.write

def find_parent(parent, x):
    # 반복문을 이용한 경로 압축
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

def main():
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

    print(str(result))

if __name__ == "__main__":
    main()