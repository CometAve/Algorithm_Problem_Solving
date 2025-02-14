T = int(input())

# 파스칼 삼각형 재귀함수로 생성
def create_pascal_with_recursive(n):
    if n == 1:
        return [1]
    else:
        prev = create_pascal_with_recursive(n-1)
        return [1]+[prev[i]+prev[i+1] for i in range(len(prev)-1)]+[1]
    
for tc in range(T):
    N = int(input())
    pascal = create_pascal_with_recursive(N)
    print(f"#{tc+1}")
    for i in range(1, N+1):
        print(" ".join(map(str, create_pascal_with_recursive(i))))