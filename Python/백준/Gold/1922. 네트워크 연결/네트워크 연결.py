# 문제 분석
# 네트워크 연결
# 각 컴퓨터를 연결하는데 필요한 최소 비용을 구하는 문제
# 입력에서 정점보다 간선의 개수가 많으므로 크루스칼 알고리즘을 사용한다.

# 입력
# N : 컴퓨터의 수 (1 ≤ N ≤ 1000)
# M : 연결할 수 있는 선의 수 (1 ≤ M ≤ 100,000)
# M개의 줄에는 연결할 컴퓨터 쌍과 비용이 주어진다.
# c : 연결 비용 (1 ≤ c ≤ 10,000)
# a, b : 같을 수도 있음

# 나의 풀이
# 크루스칼 알고리즘을 사용하여 풀이

import sys
input = sys.stdin.readline
print = sys.stdout.write

def find_parent(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x], parent)
    return parent[x]

# 두 노드를 연결
def union(x, y, parent):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    # 더 작은 노드를 부모로 설정
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
        edges.append((c, a, b))
    edges.sort()
    result = 0
    for edge in edges:
        c, a, b = edge
        if find_parent(a, parent) != find_parent(b, parent):
            union(a, b, parent)
            result += c
    
    print(str(result))

if __name__ == "__main__":
    solve()