N = 100
T = 10

for test_case in range(1, T+1):
    tc_number = int(input())
    arr = [input() for _ in range(N)]
    max_length = 0

    # 가로 방향 검사
    for i in range(N):
        row = arr[i]
        # 현재까지 찾은 최대 길이보다 큰 회문만 검사
        for k in range(N, max_length, -1):  # k: 회문의 길이 (내림차순)
            if k < 3:
                break
            found = False
            for j in range(0, N - k + 1):
                substring = row[j:j + k]
                if substring == substring[::-1]:
                    max_length = max(max_length, k)
                    found = True
                    break
            if found:  # 해당 행에서 k 길이 이상의 회문을 찾았으므로 더 짧은 길이는 볼 필요 없음
                break

    # 세로 방향 검사
    for j in range(N):
        col = ''.join(arr[i][j] for i in range(N))
        for k in range(N, max_length, -1):
            if k < 3:
                break
            found = False
            for i in range(0, N - k + 1):
                substring = col[i:i + k]
                if substring == substring[::-1]:
                    max_length = max(max_length, k)
                    found = True
                    break
            if found:
                break

    print(f'#{tc_number} {max_length}')