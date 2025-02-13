T = int(input())

# 파스칼 삼각형 재귀함수로 생성
def create_pascal_with_recursive(n):
    pascal = []
    if n == 1:
        pascal.append([1])
        return pascal
    elif n == 2:
        pascal.append([1])
        pascal.append([1, 1])
        return pascal
    else:
        prev = create_pascal_with_recursive(n-1)
        new = [1]
        for i in range(len(prev[-1])-1):
            new.append(prev[-1][i]+prev[-1][i+1])
        new.append(1)
        prev.append(new)
        return prev
    
for tc in range(T):
    N = int(input())
    pascal = create_pascal_with_recursive(N)
    print(f"#{tc+1}")
    print("\n".join([" ".join(map(str, i)) for i in pascal]))