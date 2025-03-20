import sys
input = sys.stdin.readline
print = sys.stdout.write

INF = int(1e9)

def main():
    T = int(input())
    for _ in range(T):
        N, M, W = map(int, input().split())
        edges = []
        
        for _ in range(M):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))
            edges.append((e, s, t))
        
        for _ in range(W):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))
        
        # 모든 정점을 시작점으로 간주하기 위해 초기 거리를 0으로 설정
        distance = [0] * (N+1)
        negative_cycle = False
        
        # N번 반복했을 때 여전히 갱신이 발생하면 음수 사이클 존재
        for i in range(1, N+1):
            for s, e, t in edges:
                if distance[e] > distance[s] + t:
                    distance[e] = distance[s] + t
                    if i == N:
                        # 플래그 변수로 음수 사이클 존재 여부를 확인
                        negative_cycle = True
                        break
            if negative_cycle:
                break
        
        if negative_cycle:
            print("YES\n")
        else:
            print("NO\n")

if __name__ == '__main__':
    main()