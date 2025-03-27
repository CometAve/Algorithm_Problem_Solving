import sys
input = sys.stdin.readline
INF = sys.maxsize

def solve():
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    
    # DP 테이블 초기화
    dp = [[INF] * (1 << N) for _ in range(N)]
    
    # 시작 도시는 0번
    dp[0][1] = 0  # 0번 도시만 방문한 상태
    
    # 모든 부분집합에 대해 반복
    for visited in range(1, 1 << N):
        # 시작 도시(0번)는 반드시 방문해야 함
        if not (visited & 1):
            continue
            
        # 현재 도시에 대해 반복
        for cur in range(N):
            # 현재 도시를 방문하지 않은 경우 건너뜀
            if not (visited & (1 << cur)):
                continue
                
            # 이전 방문 상태 (현재 도시를 제외한 상태)
            prev_visited = visited & ~(1 << cur)
            
            # 현재 도시가 시작 도시(0번)이고, 모든 도시를 방문한 경우 건너뜀
            if cur == 0 and prev_visited != 0:
                continue
                
            # 이전 도시에 대해 반복
            for prev in range(N):
                # 이전 도시를 방문하지 않았거나, 이전 도시에서 현재 도시로 갈 수 없는 경우 건너뜀
                if not (prev_visited & (1 << prev)) or W[prev][cur] == 0:
                    continue
                    
                # 현재 상태의 최소 비용 갱신
                dp[cur][visited] = min(dp[cur][visited], dp[prev][prev_visited] + W[prev][cur])
    
    # 모든 도시를 방문하고 시작 도시(0번)로 돌아오는 최소 비용
    result = INF
    all_visited = (1 << N) - 1
    
    for last in range(1, N):
        if W[last][0] != 0:  # 마지막 도시에서 시작 도시로 갈 수 있는 경우
            result = min(result, dp[last][all_visited] + W[last][0])
            
    return result

if __name__ == '__main__':
    sys.stdout.write(str(solve()))