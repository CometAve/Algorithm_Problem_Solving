T = int(input())

for tc in range(1, T+1):
    # 스위치 개수
    N = int(input())
    # 초기 배치
    init_form = list(map(int, input().split()))
    # 목표 배치
    target_form = list(map(int, input().split()))
    # 조작 횟수
    cnt = 0

    # 두 배열을 인덱스로 스위치 개수만큼 비교하면서 같으면 continue
    for i in range(N):
        if init_form[i] == target_form[i]:
            continue
        else:
            # 아니면 0 혹은 1로 변환하며 cnt += 1
            for j in range(i, N):
                init_form[j] ^= 1
            cnt += 1

    print(f'#{tc} {cnt}')