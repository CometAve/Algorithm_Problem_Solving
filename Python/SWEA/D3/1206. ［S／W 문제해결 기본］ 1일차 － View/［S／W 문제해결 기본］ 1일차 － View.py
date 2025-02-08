for test_case in range(1, 11):
    N = int(input())
    building_heights = list(map(int, input().split()))
     
    total_view = 0
     
    for i in range(2, N - 2):
        max_height = max(building_heights[i-2], building_heights[i-1], building_heights[i+1], building_heights[i+2])
        if building_heights[i] > max_height:
            total_view += building_heights[i] - max_height
    print(f'#{test_case} {total_view}')