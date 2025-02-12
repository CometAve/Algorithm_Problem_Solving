N = 100
 
T = 10
 
for test_case in range(1, T+1):
    tc_number = int(input())
 
    arr = [input() for _ in range(N)]
    max_length = 0
 
    for i in range(N):
        for j in range(N):
            for k in range(3, N):
                if j + k > N or i + k > N:
                    break
                word = arr[i][j:j + k]
                word = ''
                for l in range(k):
                    word += arr[i + l][j]
                if word == word[::-1]:
                    if len(word) > max_length:
                        max_length = len(word)
    print(f'#{tc_number} {max_length}')