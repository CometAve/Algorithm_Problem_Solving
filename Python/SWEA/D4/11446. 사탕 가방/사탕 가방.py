def can_make_count(x, A, M):
    # x : 만들 가방 수 후보
    # 각 사탕 종류별로 x개 가방에 몇 개씩 넣을 수 있는지 합산
    total = 0
    for candy in A:
        total += candy // x
    return total >= M

def solve():
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        # 총 사탕 수로 만들 수 있는 가방의 최대 개수는 sum(A) // M
        if sum(A) < M:
            print(f'#{tc} 0')
            continue

        lo, hi = 1, sum(A) // M
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_make_count(mid, A, M):
                ans = mid
                lo = mid + 1  # 더 많은 가방 수 가능 여부 확인
            else:
                hi = mid - 1
        print(f'#{tc} {ans}')

if __name__ == '__main__':
    solve()