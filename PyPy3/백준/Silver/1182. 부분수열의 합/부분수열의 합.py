import sys
input = sys.stdin.readline

n, S = map(int, input().split())
arr = list(map(int, input().split()))

# 남은 구간에서 만들 수 있는 최대 양수 합과 최대 음수 합을 미리 계산
suffix_pos = [0] * (n + 1)   # i번째부터 끝까지 남은 양수들의 합
suffix_neg = [0] * (n + 1)   # i번째부터 끝까지 남은 음수들의 합
for i in range(n-1, -1, -1):
    # i+1번째까지의 계산값을 이어받고, 현재 값이 양수/음수인 경우 해당 합에 더해줌
    suffix_pos[i] = suffix_pos[i+1] + (arr[i] if arr[i] > 0 else 0)
    suffix_neg[i] = suffix_neg[i+1] + (arr[i] if arr[i] < 0 else 0)

cnt = 0  # 합이 S가 되는 부분수열의 개수

def backtrack(idx, current_sum):
    global cnt
    # 종료 조건: 모든 원소를 검사한 경우
    if idx == n:
        if current_sum == S:    # 현재까지의 합이 S면 카운트
            cnt += 1
        return
    # 가지치기(pruning) 조건:
    if current_sum + suffix_pos[idx] < S:
        return  # 남은 모든 양수를 다 더해도 합이 S에 도달하지 못한다면 더 탐색할 필요 없음
    if current_sum + suffix_neg[idx] > S:
        return  # 남은 모든 음수를 다 포함해도 합을 S까지 낮추지 못한다면 탐색 중단

    # 경우 1: 현재 idx 위치의 값을 부분수열에 포함하지 않는 경우
    backtrack(idx + 1, current_sum)
    # 경우 2: 현재 idx 위치의 값을 부분수열에 포함하는 경우
    backtrack(idx + 1, current_sum + arr[idx])

backtrack(0, 0)

# 문제에서 부분수열은 "크기가 양수인 부분수열"로 한정되므로,
# 만약 S가 0이라면 공집합{}이 잘못 세어졌을 수 있어 1 감소시킴
if S == 0:
    cnt -= 1

print(cnt)