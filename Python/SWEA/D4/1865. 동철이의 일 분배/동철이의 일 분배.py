# ****아래 코드는 Claude를 통해 Top-Down 방식 DP를 개선한 코드****
def solve():
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        # 확률을 미리 0-1 사이 값으로 변환하여 저장
        P = [[int(x) / 100 for x in input().split()] for _ in range(N)]
        
        # 메모이제이션을 위한 배열 (딕셔너리보다 접근 속도가 빠름)
        memo = [-1] * (1 << N)
        
        def dfs(employee, mask):
            # 모든 직원에게 작업이 배정된 경우
            if employee == N:
                return 1.0
                
            # 이미 계산된 상태인 경우 재활용
            if memo[mask] != -1:
                return memo[mask]
            
            max_prob = 0.0
            for job in range(N):
                # 이미 배정된 작업은 건너뜀
                if mask & (1 << job):
                    continue
                    
                # 성공 확률이 0인 작업은 계산 불필요 (가지치기)
                if P[employee][job] == 0:
                    continue
                    
                # 다음 직원으로 넘어가면서 확률 갱신
                next_prob = P[employee][job] * dfs(employee + 1, mask | (1 << job))
                max_prob = max(max_prob, next_prob)
                
            # 결과를 메모이제이션에 저장
            memo[mask] = max_prob
            return max_prob
            
        result = dfs(0, 0) * 100
        print(f"#{tc} {format(result, '.6f')}")

if __name__ == '__main__':
    solve()