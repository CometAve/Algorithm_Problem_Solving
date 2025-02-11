N = 8

T = 10

for tc in range(1, T+1):
    # 우리가 찾아야 하는 회문의 길이 M
    M = int(input())

    arr = [input() for _ in range(N)]

    # 회문의 개수 (답)
    count = 0

    # 모든 위치에서 시작했을 때 길이가 M인 회문을 만들어 봐라.
    # 행번호 = i, 열번호 = j
    # 모든 위치(i, j)에서 회문을 만들어 본다. 길이 M인 회문
    # (i, j) ~ (i, j + M) => 가로 문자열 하나 만들어서 회문인지 판단
    # 행 우선 순회
    for i in range(N):
        for j in range(N - M + 1):
            word = arr[i][j:j + M]
            if word == word[::-1]:
                count += 1


    # (i, j) ~ (i + M, j) => 세로 문자열 하나 만들어서 회문인지 판단
    # 열 우선 
    for i in range(N - M + 1):
        for j in range(N):
            word = ''
            for k in range(M):
                word += arr[i + k][j]
            if word == word[::-1]:
                count += 1
    print(f'#{tc} {count}')