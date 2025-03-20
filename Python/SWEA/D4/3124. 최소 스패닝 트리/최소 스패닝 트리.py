# GPT가 개선시킨 Prim 알고리즘 코드

import heapq

def prim(V, adj):
    INF = float('inf')
    key = [INF] * (V + 1)
    mst = [False] * (V + 1)
    key[1] = 0
    hq = [(0, 1)]
    result = 0
    count = 0

    while hq and count < V:
        k, u = heapq.heappop(hq)
        
        # 이미 처리된 정점은 건너뛰기
        if mst[u]:
            continue
            
        mst[u] = True
        result += k
        count += 1

        for v, w in adj[u]:
            # 가지치기: 이미 MST에 포함된 정점은 처리하지 않음
            if not mst[v] and w < key[v]:
                key[v] = w
                heapq.heappush(hq, (w, v))
                
    # 모든 정점이 MST에 포함되었는지 확인 (그래프가 연결되지 않은 경우)
    if count < V:
        return -1  # 또는 문제에 맞는 값 반환
        
    return result

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    result = prim(V, adj)
    print(f'#{tc} {result}')