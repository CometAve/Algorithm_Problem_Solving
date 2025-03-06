# 암호코드 규칙 딕셔너리
code_dict = {
    (0, 0, 0, 1, 1, 0, 1): 0,
    (0, 0, 1, 1, 0, 0, 1): 1,
    (0, 0, 1, 0, 0, 1, 1): 2,
    (0, 1, 1, 1, 1, 0, 1): 3,
    (0, 1, 0, 0, 0, 1, 1): 4,
    (0, 1, 1, 0, 0, 0, 1): 5,
    (0, 1, 0, 1, 1, 1, 1): 6,
    (0, 1, 1, 1, 0, 1, 1): 7,
    (0, 1, 1, 0, 1, 1, 1): 8,
    (0, 0, 0, 1, 0, 1, 1): 9
}

def find_code():
    global ans
    
    for r in range(N):
        for c in range(M-1, 55, -1):  # 56개의 비트가 필요하므로 최소 인덱스는 56
            # 56개씩 잘라서 확인
            if c-56 < -1:  # 배열 범위를 벗어나면 건너뜀
                continue
            
            code = arr[r][c-55:c+1]  # 정방향으로 코드 추출
            
            # 암호코드는 모두 1로 끝남. 끝이 1이 아니면 암호코드가 아니니 건너뜀
            if code[-1] != 1:
                continue

            # 세로로 연속된 동일한 코드인지 확인
            valid = True
            for nr in range(r+1, min(r+5, N)):
                if arr[nr][c-55:c+1] != code:
                    valid = False
                    break
            
            if valid:
                # 7개씩 8번 쪼개서 암호 해독
                digits = []
                for i in range(8):
                    pattern = tuple(code[i*7:(i+1)*7])
                    if pattern in code_dict:
                        digits.append(code_dict[pattern])
                    else:
                        valid = False
                        break
                
                if valid and len(digits) == 8:
                    # 암호코드 검증: (홀수 자리 합*3 + 짝수 자리 합) % 10 == 0
                    odd_sum = digits[0] + digits[2] + digits[4] + digits[6]
                    even_sum = digits[1] + digits[3] + digits[5] + digits[7]
                    
                    if ((odd_sum * 3) + even_sum) % 10 == 0:
                        ans = sum(digits)
                    else:
                        ans = 0
                    return  # 유효한 코드를 찾으면 함수 종료

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 암호코드의 배열
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    find_code()
    print(f'#{tc} {ans}')
