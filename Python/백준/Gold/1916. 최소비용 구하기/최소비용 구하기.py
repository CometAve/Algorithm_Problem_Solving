import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, end, N, graph):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            return dist
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

def solve():
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]

    edge_dict = {}
    for _ in range(M):
        A, B, C = map(int, input().split())
        if (A, B) not in edge_dict or C < edge_dict[(A, B)]:
            edge_dict[(A, B)] = C

    for (A, B), C in edge_dict.items():
        graph[A].append((B, C))

    start, end = map(int, input().split())
    result = dijkstra(start, end, N, graph)
    sys.stdout.write(str(result))

if __name__ == "__main__":
    solve()