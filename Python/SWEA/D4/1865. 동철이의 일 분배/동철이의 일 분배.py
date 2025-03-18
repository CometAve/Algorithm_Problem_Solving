def solve():
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        P = [list(map(int, input().split())) for _ in range(N)]
        dp = {}
        def dfs(i, mask):
            if i == N:
                return 1
            if (i, mask) in dp:
                return dp[(i, mask)]
            ans = 0
            for j in range(N):
                if not (mask & (1 << j)):
                    ans = max(ans, P[i][j] / 100 * dfs(i + 1, mask | (1 << j)))
            dp[(i, mask)] = ans
            return ans
        
        result = dfs(0, 0) * 100
        result = format(result, ".6f")
        print(f"#{tc} {result}")

if __name__ == '__main__':
    solve()