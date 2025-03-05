def in_order(node):
    global word
    # node가 N보다 작거나 같을 때만 실행
    if node <= N:
        # 왼쪽 자식 노드 방문
        in_order(node * 2)
        # 단어 추가
        word += tree[node - 1][1]
        # 오른쪽 자식 노드 방문
        in_order(node * 2 + 1)
 
for tc in range(1, 11):
    N = int(input())
    # 1. 트리 생성
    tree = [input().split() for _ in range(N)]
    # 단어 저장할 변수
    word = ''
    # 2. 중위 순회
    in_order(1)
 
    print(f'#{tc} {word}')