def find_start():
    # 도착점 찾기
    y = ladder[99].index(2)
    x = 99
    
    while x > 0:
        x -= 1  # 먼저 위로 이동
        
        # 왼쪽 확인 및 이동
        if y > 0 and ladder[x][y-1]:
            while y > 0 and ladder[x][y-1]:
                y -= 1
            continue
            
        # 오른쪽 확인 및 이동
        if y < 99 and ladder[x][y+1]:
            while y < 99 and ladder[x][y+1]:
                y += 1
            continue
    
    return y

for tc in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{tc} {find_start()}')