# 문제 분석
# N개의 점원이 있고, 각 점원은 키가 다르다.
# 선반 높이 B가 주어지고, 선반 위에 올라가는 점원들의 키의 합이 B이상이어야 한다.
# 선반 위에 올라가는 점원들의 키의 합이 B이상이면서 그 차이가 최소가 되는 경우를 구하라.

# 문제 해결 방법
# 1. 점원들의 키를 오름차순으로 정렬한다.
# 2. 점원들의 키를 조합을 이용하여 B이상이 되는 경우를 찾는다.
# 부분집합 문제로 접근해야 한다. 재귀함수를 이용하여 부분집합을 구현한다.
# 가지치기 기준은 B이상이 되는 경우만 탐색한다.
# 3. B이상이 되는 경우를 찾으면 그 차이를 구한다.
# 4. 그 차이가 최소가 되는 경우를 찾는다.

# 재귀함수 + 가지치기를 사용하여 부분집합을 구현한다.
def find(idx, sum_h, cnt):
    global min_diff
    
    # 점원들의 키의 합이 B이상이면서 그 차이가 최소가 되는 경우를 찾는다.
    if sum_h >= B:
        diff = sum_h - B
        if diff < min_diff:
            min_diff = diff
        return
    
    # idx가 N과 같아지면 함수를 종료한다. (기저조건)
    if idx == N:
        return
    
    # idx번째 점원을 선택하는 경우
    find(idx+1, sum_h+H[idx], cnt+1)
    # idx번째 점원을 선택하지 않는 경우
    find(idx+1, sum_h, cnt)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 1000000 # 20명의 점원들의 키의 합은 2000이므로 1000000으로 초기화한다.

    # 점원 키 리스트 H를 오름차순으로 정렬한다.
    H.sort()

    # idx: 점원들의 키를 탐색할 인덱스
    # sum_h: 점원들의 키의 합
    # cnt: 점원들의 수
    idx = 0
    sum_h = 0
    cnt = 0

    find(idx, sum_h, cnt)
    print(f'#{tc} {min_diff}')