T = int(input())

# 파스칼 삼각형을 재귀적으로 생성하는 함수.
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
        # n이 3 이상이면, 먼저 n-1 행까지의 파스칼 삼각형을 재귀 호출로 생성.
        prev = create_pascal_with_recursive(n-1)
        # 새로 만들 행은 항상 1로 시작함.
        new = [1]
        
        # for문: 이전 행(prev[-1])의 숫자들을 순차적으로 접근
        # 범위: range(len(prev[-1]) - 1)
        #   - 이전 행의 길이가 L일 때, 인접한 두 숫자를 더해야 하므로 0부터 L-2까지 인덱스를 사용.
        # 예를 들어, 이전 행이 [1, 3, 3, 1] (길이 4)라면, i는 0, 1, 2로 진행됨.
        #   i=0: 1 + 3 = 4
        #   i=1: 3 + 3 = 6
        #   i=2: 3 + 1 = 4
        for i in range(len(prev[-1]) - 1):
            # 공식: 새 행의 중간 값은 이전 행의 인접한 두 수의 합.
            new.append(prev[-1][i] + prev[-1][i+1])
        
        # 새 행의 마지막 값은 항상 1.
        new.append(1)
        # 새로 생성된 행을 이전 삼각형에 덧붙임.
        prev.append(new)
        return prev

for tc in range(T):
    N = int(input())  # 예: 각 테스트 케이스마다 삼각형의 행 수를 입력받음. 예를 들어, 5
    
    pascal = create_pascal_with_recursive(N)
    
    print(f"#{tc+1}")
    
    # 리스트 내포를 사용하여 각 행을 문자열로 변환하고, 개행 문자로 이어 붙여 전체 삼각형 출력.
    # 예를 들어, N=5 인 경우 출력:
    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1
    # 1 4 6 4 1
    print("\n".join([" ".join(map(str, row)) for row in pascal]))
