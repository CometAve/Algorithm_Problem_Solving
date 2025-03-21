# 감사합니다 지선생 전 단순한 오류를 못 찾고 있었네요. AI최고
def solution():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        synergy = [list(map(int, input().split())) for _ in range(N)]
        min_diff = float('inf')
        A, B = [], []

        def divide(idx):
            nonlocal min_diff
            if idx == N:
                if len(A) == N//2 and len(B) == N//2:
                    taste_A = 0
                    taste_B = 0
                    for i in A:
                        for j in A:
                            taste_A += synergy[i][j]
                    for i in B:
                        for j in B:
                            taste_B += synergy[i][j]
                    min_diff = min(min_diff, abs(taste_A - taste_B))
                return

            # 가지치기 A, B의 개수가 N/2가 되면 return
            if len(A) > N//2 or len(B) > N//2:
                return
            
            # A가 아직 덜 찼다면 A에 추가
            if len(A) < N//2:
                A.append(idx)
                divide(idx+1)
                A.pop()

            # B가 아직 덜 찼다면 B에 추가
            if len(B) < N//2:
                B.append(idx)
                divide(idx+1)
                B.pop()
        
        divide(0)
        print(f'#{tc} {min_diff}')

if __name__ == '__main__':
    solution()