# 접근 방법:
# 1. 각 방에서 시작해서 연속적으로 이동할 수 있는 방의 최대 개수를 구한다
# <이전 코드와 차이점>
# 2. DFS와 메모이제이션을 활용하여 각 위치에서 이동 가능한 최대 방의 개수를 계산한다
# 3. 가지치기 최적화를 통해 불필요한 탐색을 줄인다:
#    - 방 번호 기준 정렬을 통해 효율적 탐색
#    - 현재 알고 있는 최대값을 넘을 수 없는 경우 탐색 중단
#    - 이미 방문한 위치는 재계산하지 않음(메모이제이션)
# 4. 최대로 많은 방을 이동할 수 있는 시작점 중 방 번호가 가장 작은 것을 찾는다


# 상하좌우 방향 이동을 위한 델타 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 메모이제이션을 활용한 DFS - 각 위치에서 최대로 몇 개의 방을 이동할 수 있는지 계산
def dfs(x, y, depth=1):
    # 재귀 깊이가 현재 알고 있는 최대값보다 크면 가지치기
    global max_cnt
    if depth + (N*N - rooms[x][y]) < max_cnt:  # 가지치기 조건: 남은 모든 값을 방문해도 최대값 못 넘을 경우
        return depth
    
    # 이미 계산한 위치라면 저장된 값 반환 (메모이제이션)
    if dp[x][y] != 0:
        return dp[x][y]
    
    # 현재 방에서 시작하는 경우 최소 1개 방문 가능
    max_move = 1
    
    # 상하좌우 네 방향 탐색
    found_next = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 격자 범위 내에 있고, 현재 방보다 정확히 1 큰 번호를 가진 방이면 이동
        if 0 <= nx < N and 0 <= ny < N and rooms[nx][ny] == rooms[x][y] + 1:
            found_next = True
            # 다음 방에서 이동할 수 있는 최대 방의 수 + 1 (현재 방)
            max_move = max(max_move, dfs(nx, ny, depth+1) + 1)
    
    # 다음 방이 없다면 더 탐색할 필요 없음 (가지치기)
    if not found_next:
        dp[x][y] = 1
        return 1
    
    # 결과 저장 후 반환 (메모이제이션)
    dp[x][y] = max_move
    return max_move

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    
    # 메모이제이션을 위한 배열 초기화
    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    max_cnt = 0          # 최대 이동 가능한 방의 개수
    min_room_num = 10 ** 3
    
    # 가지치기 최적화: 방 번호 기준으로 정렬하여 큰 숫자부터 탐색
    room_positions = []
    for i in range(N):
        for j in range(N):
            room_positions.append((rooms[i][j], i, j))
    
    # 값이 작은 방부터 탐색 (작은 값이 긴 연속 수열의 시작점일 가능성이 높음)
    room_positions.sort()
    
    for num, i, j in room_positions:
        # 방 번호가 크면 최대 이동 가능 거리가 짧아짐 (가지치기)
        if num > N*N - max_cnt + 1:
            continue
            
        # 해당 위치에서 시작했을 때 이동 가능한 최대 방의 개수
        cnt = dfs(i, j)
        
        # 최대 이동 수가 갱신되면 방 번호도 갱신
        if cnt > max_cnt:
            max_cnt = cnt
            min_room_num = rooms[i][j]
        # 최대 이동 수가 같다면 방 번호가 더 작은 것 선택
        elif cnt == max_cnt and rooms[i][j] < min_room_num:
            min_room_num = rooms[i][j]
    
    print(f'#{tc} {min_room_num} {max_cnt}')