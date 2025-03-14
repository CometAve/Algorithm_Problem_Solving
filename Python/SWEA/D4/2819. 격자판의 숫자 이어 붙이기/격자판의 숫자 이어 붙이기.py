T = int(input())

for tc in range(1, T+1):
    N = 4 # 4x4 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 4x4 배열을 돌면서 7자리 수를 만들 수 있는지 확인
    ans = set() # 중복을 제거하기 위해 set 사용
    for i in range(N):
        for j in range(N):
            stack = [(i, j, 0, arr[i][j])] # x, y, cnt, num
            while stack:
                x, y, cnt, num = stack.pop()
                if cnt == 6:
                    ans.add(num)
                    continue
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        stack.append((nx, ny, cnt+1, num*10+arr[nx][ny]))
    print(f'#{tc} {len(ans)}')