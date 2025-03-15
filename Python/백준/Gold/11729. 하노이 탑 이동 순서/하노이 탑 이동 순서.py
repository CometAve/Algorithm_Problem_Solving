def hanoi(n, a, b, c): # n개의 원판을 a에서 c로 옮기는 함수
    if n == 1: # 원판이 1개인 경우
        print(a, c)
    else:
        hanoi(n-1, a, c, b) # n-1개의 원판을 a에서 b로 옮김
        print(a, c)
        hanoi(n-1, b, a, c) # n-1개의 원판을 b에서 c로 옮김

n = int(input())
print(2**n-1) # 이동 횟수
hanoi(n, 1, 2, 3)