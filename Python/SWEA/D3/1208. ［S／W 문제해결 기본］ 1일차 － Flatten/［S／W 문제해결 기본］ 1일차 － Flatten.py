for test_case in range(1, 11):
    N = int(input())
    box_heights = list(map(int, input().split()))
 
    # N번의 dump 작업을 수행
    for _ in range(N):
        # 가장 높은 상자와 가장 낮은 상자의 인덱스를 찾는다.
        max_box_idx = 0
        min_box_idx = 0
        for i in range(1, 100):
            if box_heights[i] > box_heights[max_box_idx]:
                max_box_idx = i
            if box_heights[i] < box_heights[min_box_idx]:
                min_box_idx = i
 
        # 높이가 가장 높은 상자와 가장 낮은 상자의 높이를 조정
        box_heights[max_box_idx] -= 1
        box_heights[min_box_idx] += 1
 
        # 높이 차이가 1이면 종료
        if box_heights[max_box_idx] - box_heights[min_box_idx] <= 1:
            break
 
    # 가장 높은 상자와 가장 낮은 상자를 다시 찾아서 높이 차이 계산
    max_height = box_heights[0]
    min_height = box_heights[0]
    for height in box_heights:
        if height > max_height:
            max_height = height
        if height < min_height:
            min_height = height
 
    print(f'#{test_case} {max_height - min_height}')