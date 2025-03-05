def in_order(node, tree_dict, max_node, result):
    if node > max_node:
        return
    
    # 왼쪽 자식 노드가 있으면 방문
    if 2*node <= max_node:
        in_order(node*2, tree_dict, max_node, result)
    
    # 현재 노드의 값 추가
    result.append(tree_dict[node])
    
    # 오른쪽 자식 노드가 있으면 방문
    if 2*node+1 <= max_node:
        in_order(node*2+1, tree_dict, max_node, result)

for tc in range(1, 11):
    N = int(input())
    
    # 딕셔너리로 트리 저장
    tree_dict = {}
    for i in range(1, N+1):
        info = input().split()
        tree_dict[int(info[0])] = info[1]
    
    # 단어 저장할 리스트
    result = []
    
    # 중위 순회
    in_order(1, tree_dict, N, result)
    
    print(f'#{tc} {"".join(result)}')