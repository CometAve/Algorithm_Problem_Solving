from heapq import heappush, heappop

def dijkstra(start, N, graph):
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[start] = 0
    q = []
    heappush(q, (0, start))
    while q:
        cost, node = heappop(q)
        if cost > dist[node]:
            continue
        for nxt, weight in graph[node]:
            if cost + weight < dist[nxt]:
                dist[nxt] = cost + weight
                heappush(q, (dist[nxt], nxt))
    return dist

def main():
    T = int(input())
    for tc in range(1, T+1):
        N, M, X = map(int, input().split())
        graph = [[] for _ in range(N+1)]
        rev_graph = [[] for _ in range(N+1)]
        for _ in range(M):
            u, v, w = map(int, input().split())
            graph[u].append((v, w))
            rev_graph[v].append((u, w))
        
        dist_from_X = dijkstra(X, N, graph)
        dist_to_X = dijkstra(X, N, rev_graph)
        result = 0
        for i in range(1, N+1):
            result = max(result, dist_from_X[i] + dist_to_X[i])
        print(f'#{tc} {result}')

if __name__ == "__main__":
    main()