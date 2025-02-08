for test_case in range(1, 11):
    N = int(input())
    box_heights = list(map(int, input().split()))
  
    # 조건
    # 박스들의 가로 길이는 항상 100
    # 작업 제한 횟수를 다 사용하면 작업종료
    # dump란 가장 높은 상자를 가장 낮은 상자 위로 옮기는 작업
    # dump를 할 때마다 가장 높은 상자와 가장 낮은 상자를 갱신
    # dump를 할 때마다 가장 높은 상자와 가장 낮은 상자의 높이 차이가 1 이하일 때 작업종료
  
    for i in range(N):
        max_height = 0
        min_height = 100
        # 가장 높은 상자와 가장 낮은 상자의 위치를 찾는다.
        for j in range(100):
            if box_heights[j] > max_height:
                max_height = box_heights[j]
            if box_heights[j] < min_height:
                min_height = box_heights[j]
  
        # 가장 높은 상자와 가장 낮은 상자의 위치 차이가 0을 이상일 때
        if max_height - min_height > 0:
            # 가장 높은 상자의 위치에서 1을 빼고 가장 낮은 상자의 위치에서 1을 더한다.
            box_heights[box_heights.index(max_height)] -= 1
            box_heights[box_heights.index(min_height)] += 1
  
        # 가장 높은 상자와 가장 낮은 상자의 위치 차이가 0 일 때
        if max_height - min_height == 0:
            break
         
    print(f'#{test_case} {max(box_heights) - min(box_heights)}')