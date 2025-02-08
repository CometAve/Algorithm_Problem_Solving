for test_case in range(1, 11):
    N = int(input())
    box_heights = list(map(int, input().split()))
     
    for _ in range(N):
        box_heights = sorted(box_heights)
        box_heights[0] += 1
        box_heights[-1] -= 1
        if box_heights[-1] - box_heights[0] <= 1:
            break
    box_heights = sorted(box_heights)   
    print(f'#{test_case} {box_heights[-1] - box_heights[0]}')