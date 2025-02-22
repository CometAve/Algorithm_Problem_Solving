import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs_set(node, graph, memo):
    if node in memo:
        return memo[node]
    # 자기 자신 포함
    reachable_set = {node}
    for nxt in graph[node]:
        # 집합의 합집합(union)으로 중복된 노드가 포함되지 않도록 함
        reachable_set |= dfs_set(nxt, graph, memo)
    memo[node] = reachable_set
    return reachable_set

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

memo_forward = {}
memo_reverse = {}
result = 0

# 각 학생 i에 대해, 자신보다 키가 큰 집합(taller)과 키가 작은 집합(shorter)을 구함.
for i in range(1, N + 1):
    taller = dfs_set(i, graph, memo_forward)
    shorter = dfs_set(i, reverse_graph, memo_reverse)
    # 자기 자신이 중복되었으므로 -1 해주면 전체 비교 가능한 학생 수가 N-1이면 순서를 확실히 알 수 있음
    if len(taller) + len(shorter) - 1 == N:
        result += 1

print(result)