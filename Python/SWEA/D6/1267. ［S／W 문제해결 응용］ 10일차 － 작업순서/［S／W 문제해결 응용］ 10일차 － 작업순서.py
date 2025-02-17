T = 10

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for w in graph[v]:
        for s in prev_node[w]:
            if not visited[s]:
                break
        else:
            if not visited[w]:
              dfs(w)

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    
    # 인접 리스트로 그래프와 각 노드의 이전 노드를 초기화
    graph = [[] for _ in range(V + 1)]
    prev_node = [[] for _ in range(V + 1)]
    
    for i in range(E):
        v, e = edges[i * 2], edges[i * 2 + 1]
        graph[v].append(e)
        prev_node[e].append(v)

    visited = [False] * (V + 1)

    print(f'#{test_case}', end=' ')
    # 이전 노드가 없는 노드를 찾아서 시작 노드로 지정하여 함수 호출
    for i in range(1, V + 1):
        if not prev_node[i]:
            dfs(i)
    print()