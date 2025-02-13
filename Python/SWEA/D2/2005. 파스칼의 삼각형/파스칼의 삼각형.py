T = int(input())

def create_pascal(n):
    pascal = [[1]]
    for i in range(1, n):
        pascal.append([1])
        for j in range(1, i):
            pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
        pascal[i].append(1)
    return pascal

for tc in range(T):
    N = int(input())
    pascal = create_pascal(N)
    print(f"#{tc+1}")
    for i in range(N):
        print(" ".join(map(str, pascal[i])))