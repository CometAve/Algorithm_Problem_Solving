import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

def dijkstra(start, end, distance, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
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
    distance = [int(1e9)] * (N+1)

    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))

    start, end = map(int, input().split())
    print(str(dijkstra(start, end, distance, graph)))

if __name__ == "__main__":
    solve()