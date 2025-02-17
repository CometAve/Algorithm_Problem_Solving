def get_position(wait_num, C, R):
    if wait_num > C * R:
        return 0
    
    position_map = [[0] * C for _ in range(R)]
    
    count = 1
    x, y = R-1, 0
    position_map[x][y] = count
    
    if count == wait_num:
        return (y+1, R-x)
    
    dx, dy = -1, 0
    while count < wait_num:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and position_map[nx][ny] == 0:
            x, y = nx, ny
        else:
            dx, dy = dy, -dx
            x, y = x + dx, y + dy
        count += 1
        position_map[x][y] = count
        if count == wait_num:
            return (y+1, R-x)
        
C, R = map(int, input().split())
wait_num = int(input())
result = get_position(wait_num, C, R)
if result == 0:
    print(result)
else:
    print(result[0], result[1])