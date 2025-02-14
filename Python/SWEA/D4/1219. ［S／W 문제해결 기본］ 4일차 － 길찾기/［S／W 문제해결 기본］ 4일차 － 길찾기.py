T = 10

def dfs(s):
    visited[s] = 1
    route.append(s)
    if s == 99:
        return 1
    for i in graph[s]:
        if not visited[i]:
            if dfs(i):
                return 1
    route.pop()
    return 0

for _ in range(1, T+1):
    tc, E = map(int, input().split())
    path = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    route = [] # stack
    visited = [0] * 100
    for i in range(0, E*2, 2):
        graph[path[i]].append(path[i+1])
    print(f'#{tc} {dfs(0)}')