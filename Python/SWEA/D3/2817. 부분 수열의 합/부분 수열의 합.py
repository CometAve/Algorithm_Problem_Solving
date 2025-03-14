# 문제 분석
# 부분 수열의 합이 K가 되는 경우의 수를 구하는 문제
# 부분 수열을 구하는 방법은 재귀를 이용해서 구할 수 있다.
# 가지치기 조건은 부분 수열의 합이 K를 넘어가면 더 이상 탐색하지 않도록 한다.

# 문제 해결 방법
def subset(idx, sum):
    global cnt
    if sum > K:
        return
    if idx == N:
        if sum == K:
            cnt += 1
        return
    subset(idx+1, sum+sequence[idx])
    subset(idx+1, sum)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))

    cnt = 0
    
    subset(0, 0)

    print(f'#{tc} {cnt}')
