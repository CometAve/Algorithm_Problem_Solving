# 예산
# 문제 분석
# 정해진 총액 이하에서 가능한 최대의 총 예산을 구하는 문제
# Parametric Search를 이용하여 최적의 값을 찾아야 한다.

# 수도코드
# 1. 입력값을 받는다.
# 2. 입력값을 정렬한다.
# 3. Parametric Search를 이용하여 최적의 값을 찾는다.
# 3-1. left = 0, right = budgets[-1]로 초기화한다.
# 3-2. left <= right일 때까지 반복한다.
# 3-3. mid = (left + right) // 2로 설정한다.
# 3-4. total = 0으로 초기화한다.
# 3-5. 각 budget에 대해, min(budget, mid)를 total에 더한다.
# 3-6. total이 total_budget보다 작거나 같으면, answer = mid로 설정하고 left = mid + 1로 설정한다.
# 3-7. total이 total_budget보다 크면, right = mid - 1로 설정한다.
# 4. 결과를 출력한다.

# 시간 복잡도: O(NlogN)
# - 입력값을 정렬하는 부분이 O(NlogN)이다.
# - Parametric Search를 이용하여 최적의 값을 찾는 부분이 O(logN)이다.
# - 따라서, 전체 시간 복잡도는 O(NlogN)이다.

def solve():
    n = int(input())
    budgets = list(map(int, input().split()))
    total_budget = int(input())

    budgets.sort()

    left = 0
    right = budgets[-1] 
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for budget in budgets:
            total += min(budget, mid)
        if total <= total_budget:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

if __name__ == "__main__":
    solve()