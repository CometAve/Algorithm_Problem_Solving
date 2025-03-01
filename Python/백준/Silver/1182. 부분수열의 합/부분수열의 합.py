import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def dfs(idx, current_sum):
    global cnt
    # 종료조건: 모든 원소에 대해 결정했다면 종료
    if idx == n:
        return

    # 남은 원소들로 만들 수 있는 최대/최소 추가값 계산
    remaining_positive = sum(x for x in arr[idx:] if x > 0)
    remaining_negative = sum(x for x in arr[idx:] if x < 0)
    
    # 가지치기 조건:
    # 1) current_sum이 s보다 작은데, 남은 원소들을 모두 더해도 s에 미치지 못하면 더 볼 필요 없음.
    if current_sum < s and current_sum + remaining_positive < s:
        return
    # 2) current_sum이 s보다 큰데, 남은 원소들을 모두 더해(음의 값만 고려)도 s보다 크면 더 볼 필요 없음.
    if current_sum > s and current_sum + remaining_negative > s:
        return

    # 현재 원소를 선택하는 경우
    new_sum = current_sum + arr[idx]
    if new_sum == s:
        cnt += 1
    dfs(idx + 1, new_sum)
    
    # 현재 원소를 선택하지 않는 경우
    dfs(idx + 1, current_sum)

dfs(0, 0)
print(cnt)