for test_case in range(1, 11):
    N = int(input())
    building_list = list(map(int, input().split()))
    total_view = 0
    for i in range(2, N - 2):
 
        building_heights_list = building_list[i - 2:i + 3]
        building_heights_list.pop(2)
 
        highest = 0
        for height in building_heights_list:
            if height > highest:
                highest = height
 
        if building_list[i] > highest:
            total_view += (building_list[i] - highest)
    print(f'#{test_case} {total_view}')