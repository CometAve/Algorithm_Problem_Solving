for test_case in range(1, 11):
    N = int(input())
    box_heights = list(map(int, input().split()))
     
    for i in range(N):
        if max(box_heights) - min(box_heights) <= 1:
            break
             
        max_idx = box_heights.index(max(box_heights))
        min_idx = box_heights.index(min(box_heights))
         
        box_heights[max_idx] -= 1
        box_heights[min_idx] += 1
     
    print(f'#{test_case} {max(box_heights) - min(box_heights)}')