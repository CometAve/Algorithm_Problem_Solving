def solve():
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        edges = list(map(int, input().split()))
        graph = [[] for _ in range(N+1)]
        for i in range(M):
            u = edges[2*i]
            v = edges[2*i+1]
            graph[u].append(v)
            
        S, G = map(int, input().split())
        
        count = 0
        visited = [False] * (N+1)
        
        def dfs(current):
            nonlocal count
            if current == G:
                count += 1
                return
            for nxt in graph[current]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dfs(nxt)
                    visited[nxt] = False
        
        visited[S] = True
        dfs(S)
        print(f"#{tc} {count}")

if __name__ == '__main__':
    solve()