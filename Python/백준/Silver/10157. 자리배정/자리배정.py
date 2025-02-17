import sys
input = sys.stdin.readline

def get_position(wait_num, C, R):
    total_seats = C * R
    if wait_num > total_seats:
        return 0

    # 경계 설정 (행: 0 ~ R-1, 열: 0 ~ C-1)
    top, bottom = 0, R - 1
    left, right = 0, C - 1

    # 시작 좌표 (왼쪽 맨 아래)
    x, y = bottom, left
    count = 1
    if count == wait_num:
        return (y + 1, R - x)
    
    # 좌석 배정은 반시계가 아닌, 시계방향의 "나선" (spiral) 순서로 진행됨
    # 이동 순서: 위 -> 오른쪽 -> 아래 -> 왼쪽
    while True:
        # 1. 위쪽으로 이동 (현재 x -> top)
        steps = x - top
        if wait_num <= count + steps:
            new_x = x - (wait_num - count)
            return (y + 1, R - new_x)
        count += steps
        x = top  # 꼭대기로 이동
        left += 1  # 왼쪽 열은 모두 채워졌으므로 경계 조정
        if left > right or top > bottom:
            break

        # 2. 오른쪽으로 이동 (현재 y -> right)
        steps = right - y
        if wait_num <= count + steps:
            new_y = y + (wait_num - count)
            return (new_y + 1, R - x)
        count += steps
        y = right
        top += 1  # 위쪽 행이 채워졌으므로 경계 조정
        if left > right or top > bottom:
            break

        # 3. 아래쪽으로 이동 (현재 x -> bottom)
        steps = bottom - x
        if wait_num <= count + steps:
            new_x = x + (wait_num - count)
            return (y + 1, R - new_x)
        count += steps
        x = bottom
        right -= 1  # 오른쪽 열 채움
        if left > right or top > bottom:
            break

        # 4. 왼쪽으로 이동 (현재 y -> left)
        steps = y - left
        if wait_num <= count + steps:
            new_y = y - (wait_num - count)
            return (new_y + 1, R - x)
        count += steps
        y = left
        bottom -= 1  # 아래쪽 행 채움
        if left > right or top > bottom:
            break

    # 정상적으로 좌석을 할당하는 경우 여기까지 오지 않습니다.
    return 0

C, R = map(int, input().split())
wait_num = int(input())
result = get_position(wait_num, C, R)
if result == 0:
    print(result)
else:
    print(result[0], result[1])