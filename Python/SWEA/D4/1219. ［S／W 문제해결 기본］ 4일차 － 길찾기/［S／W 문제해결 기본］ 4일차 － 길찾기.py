T = 10

def dfs(s):
    if s == 99:
        return 1
    if memo[s] is not None:
        return memo[s]
    visited[s] = True  # 현재 경로 방문 체크 (사이클 방지)
    found = 0
    for nxt in graph[s]:
        if not visited[nxt]:
            if dfs(nxt):
                found = 1
                break
    visited[s] = False  # 재귀 종료 후 방문체크 해제
    memo[s] = found
    return found

for _ in range(1, T+1):
    tc, E = map(int, input().split())
    path = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    memo = [None] * 100  # 각 노드에서 목표(99)에 도달 가능한지 여부 캐싱
    visited = [False] * 100
    for i in range(0, E*2, 2):
        graph[path[i]].append(path[i+1])
    print(f'#{tc} {dfs(0)}')