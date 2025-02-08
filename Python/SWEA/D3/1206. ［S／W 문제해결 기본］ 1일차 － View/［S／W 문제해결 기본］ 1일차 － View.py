for test_case in range(1, 11):
    N = int(input())
    building_heights = list(map(int, input().split()))
      
    total_view = 0
      
    for i in range(2, N - 2):
      highest = 0
      for j in range(i - 2, i + 3):
        if j != i:
          if building_heights[j] > highest:
            highest = building_heights[j]
      if building_heights[i] > highest:
        total_view += building_heights[i] - highest
          
    print(f'#{test_case} {total_view}')