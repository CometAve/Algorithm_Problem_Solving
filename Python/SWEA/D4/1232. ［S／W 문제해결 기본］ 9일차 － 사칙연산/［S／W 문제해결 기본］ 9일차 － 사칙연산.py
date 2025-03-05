def postorder(t):
    # t번 노드가 숫자면 실수로 바꿔서 리턴한다. (부모노드에서 사용 가능)
    if node[t] not in '+-*/':
        return float(node[t])
    # t번 노드가 연산자면 계산
    else:
        # 연산에 알맞은 순회 방법은?
        # hint) 연산자는 피연산자가 있어야 연산 가능
        # 수식 트리의 좌측 자식 노드와 우측 자식 노드가 다 숫자여야 가능
        # 연산 결과 다른 연산자가 또 다시 써야하니 리턴
        left = postorder(int(cleft[t]))
        right = postorder(int(cright[t]))
        if node[t] == '+':
            return left + right
        elif node[t] == '-':
            return left - right
        elif node[t] == '*':
            return left * right
        elif node[t] == '/':
            return left / right
        else:
            return node[t]


T = 10

for tc in range(1, T + 1):
    N = int(input())

    # cleft[p] => p번 노드의 왼쪽 자식 노드 번호
    # cright[p] => p번 노드의 오른쪽 자식 노드 번호
    cleft = [0] * (N + 1)
    cright = [0] * (N + 1)

    # 피연산자나, 연산자를 저장할 배열
    # node[i] => i번 노드에 저장된 연산자 혹은 피연산자
    node = [0] * (N + 1)

    for i in range(N):
        info = input().split()

        # 노드의 번호
        n = int(info[0])

        # 읽어온 줄의 2번쨰(1번인덱스) 에 있는 글자가 숫자인가 ? 연산자인가 ? 판단하고
        if info[1] in '+-*/':
        # n번 노드에 피연산자 or 연산자 저장
            node[n] = info[1]
        # 연산자 라면 왼쪽 자식 노드와 오른쪽 자식 노드도 저장
            cleft[n] = info[2]
            cright[n] = info[3]
        else:
            node[n] = info[1]


    # 답 구하고 출력
    print(f'#{tc} {int(postorder(1))}')