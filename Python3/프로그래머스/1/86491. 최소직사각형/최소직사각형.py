def solution(sizes):
    # 배열 길이
    N = len(sizes)
    
    # 가로, 세로 최대 크기 변수 / 넓이 변수
    longest_width = 0
    longest_height = 0
    area = 0
    
    # 가로 길이가 세로 길이보다 짧다면 값 교환(=회전)
    for i in range(N):
        # size[i][0] = 가로, size[i][1] = 세로
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    
    # 가장 긴 가로 길이 구하기
    for w in range(N):
        if sizes[w][0] > longest_width:
            longest_width = sizes[w][0]
            
    # 가장 긴 세로 길이 구하기
    for h in range(N):
        if sizes[h][1] > longest_height:
            longest_height = sizes[h][1]
    
    area = longest_width * longest_height
    
    return area