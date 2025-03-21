import heapq

def solution():
    T = int(input())

    for tc in range(1, T+1):
        n = int(input())
        x_coord = list(map(int, input().split()))
        y_coord = list(map(int, input().split()))
        # 환경 부담 실수 세율
        tax = float(input())
        # Prim 알고리즘을 사용하기 위해 인접행렬을 만들어준다.
        adj = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                adj[i][j] = (x_coord[i] - x_coord[j])**2 + (y_coord[i] - y_coord[j])**2

        INF = float('inf')
        key = [INF] * n
        mst = [False] * n

        pq = []
        key[0] = 0
        heapq.heappush(pq, (0, 0))

        result = 0
        count = 0  # MST에 포함된 정점 수
        while pq:
            k, u = heapq.heappop(pq)
            if mst[u]:
                continue
            if k > key[u]:
                continue

            mst[u] = True
            result += k
            count += 1
            if count == n:
                break

            for v in range(n):
                if not mst[v] and adj[u][v] < key[v]:
                    key[v] = adj[u][v]
                    heapq.heappush(pq, (key[v], v))

        print(f'#{tc} {round(result * tax)}')

if __name__ == '__main__':
    solution()