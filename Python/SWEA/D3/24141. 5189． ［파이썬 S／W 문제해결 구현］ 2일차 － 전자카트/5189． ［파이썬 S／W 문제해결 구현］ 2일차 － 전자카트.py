# 설계
# 순열을 구하는 재귀함수를 만들어서 구현한다.
# 방문한 구역을 체크하기 위한 리스트 visited를 만들어서 방문한 구역은 1로 체크한다.
# 왜냐하면 모든 구역을 한번씩만 방문해야 하기 때문이다.
# 최소 배터리 사용량을 저장할 변수 minV를 만든다.
# 순열을 구할 재귀함수 perm을 만든다.
# perm함수의 인자로 k, n, s를 받는다.
# k는 순열의 길이, n은 구역의 수, s는 배터리 사용량을 누적해서 저장한다.
# 모든 구역을 방문했을 때, 마지막 구역에서 사무실로 돌아가는 배터리 사용량을 더해준다.
# 최소값을 비교해서 저장한다.
# 가지치기를 위해 현재까지의 사용량이 최사용량 보다 크거나 같으면 리턴한다.

# 순열을 구할 재귀함수
def perm(k, n, s, e, visited, order, minV):
    # 모든 구역을 방문했을 때
    if k == n:
        # 마지막 구역에서 사무실로 돌아가는 배터리 사용량을 더해준다.
        s += e[order[-1]][0]
        # 최소값 반환
        return min(minV, s)
    # 가지치기 - 현재까지의 사용량이 최소 사용량 보다 크거나 같으면 리턴
    elif s >= minV:
        return minV
    else:
        # 순열을 구할 재귀함수
        for i in range(1, n):
            if visited[i] == 0:
                visited[i] = 1
                order[k] = i
                # 재귀함수 호출 - 다음 구역으로 이동 - k+1, n, s+e[order[k-1]][i] - 현재까지의 사용량에 현재 구역에서 다음 구역으로 이동하는 배터리 사용량을 더해준다.
                minV = perm(k+1, n, s+e[order[k-1]][i], e, visited, order, minV)
                visited[i] = 0
        return minV

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    # 방문한 구역을 체크하기 위한 리스트
    visited = [0] * N
    # 첫번째 구역은 방문했다고 체크
    visited[0] = 1
    # 최소 배터리 사용량을 저장할 변수
    minV = 100 * N
    # 순열을 저장할 리스트
    order = [0] * N
    # 첫번째 구역을 시작으로 순열을 구한다.
    minV = perm(1, N, 0, e, visited, order, minV)
    print(f'#{tc} {minV}')