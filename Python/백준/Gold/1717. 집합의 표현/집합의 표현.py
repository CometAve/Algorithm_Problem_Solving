import sys
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    # m : 연산의 개수, n : 집합의 개수
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    # 경로 압축(Path Compression)
    # find 함수를 호출할 때마다 경로를 압축해서
    # 루트 노드를 찾아야 한다
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    # Union-by-rank
    # rank를 이용해서 두 집합을 합칠 때
    # 높이가 낮은 트리를 높은 트리에 붙이는 방식
    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return
        
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
                
    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print("YES\n")
            else:
                print("NO\n")

if __name__ == '__main__':
    solve()