T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 학생 수
    list = [0] * 201  # 복도 사용 현황을 기록할 배열 (최대 200개의 복도 구간)
    
    for i in range(N):
        a, b = map(int, input().split())  # 현재 방(a)과 돌아갈 방(b) 입력
        
        # 방 번호 정렬: 항상 작은 방에서 큰 방 방향으로 계산하도록 함
        if a > b:
            a, b = b, a
        
        # 방 번호를 복도 구간 번호로 변환하여 카운팅
        # 수련회 하는 곳 구조: 1-2번방은 1번 복도, 3-4번방은 2번 복도... 이런 식으로
        # 방 번호가 1~400이므로 (방번호+1)//2로 복도 번호(1~200)로 변환
        # 예: 방1,2 -> 복도1, 방3,4 -> 복도2, 방5,6 -> 복도3...
        for j in range((a+1)//2, (b+1)//2+1):
            list[j] += 1  # 해당 복도 구간을 사용했으므로 카운트 증가
    
    # 가장 많이 사용된 복도 구간의 사용 횟수 = 필요한 최소 시간
    # (복도는 한 번에 한 명만 지나갈 수 있으므로)
    print('#%d %d' % (tc, max(list)))