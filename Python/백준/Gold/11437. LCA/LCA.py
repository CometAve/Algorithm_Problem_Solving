import sys
from collections import deque
input = sys.stdin.readline

# 일단 N을 받아.
N = int(input())
# 트리 생성 - 인접 리스트(양방향)
tree = [[] for _ in range(N+1)]
for _ in range(N-1): # N-1개의 간선 정보를 받아서 트리 생성
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)  # 양방향 연결

# Binary Lifting을 위한 준비
LOG = 16  # 2^16 > 65,000 (최대 노드 수)
parent = [[0] * (N+1) for _ in range(LOG)]
depth = [0] * (N+1)
visited = [False] * (N+1)

# BFS로 각 노드의 깊이와 첫 번째 부모 계산
def calculate_depth():
    queue = deque([(1, 0)])  # (노드, 깊이) 튜플로 큐에 삽입
    visited[1] = True
    
    while queue:
        node, d = queue.popleft()
        depth[node] = d
        
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[0][neighbor] = node  # 바로 위 부모 저장
                queue.append((neighbor, d+1))

calculate_depth()

# Binary Lifting - 희소 테이블 구성
def preprocess():
    for i in range(1, LOG):
        for j in range(1, N+1):
            # j의 2^i번째 조상 = (j의 2^(i-1)번째 조상)의 2^(i-1)번째 조상
            parent[i][j] = parent[i-1][parent[i-1][j]]

preprocess()

# LCA 찾기 (Binary Lifting 사용)
def find_lca(node1, node2):
    # 깊이가 더 깊은 노드를 deeper로, 더 얕은 노드를 shallower로 설정
    if depth[node1] > depth[node2]:
        node1, node2 = node2, node1
    
    # 깊이 맞추기 (Binary Lifting)
    diff = depth[node2] - depth[node1]
    for i in range(LOG-1, -1, -1):
        if diff & (1 << i):
            node2 = parent[i][node2]
    
    # 이미 같은 노드라면 바로 반환
    if node1 == node2:
        return node1
    
    # 공통 조상 찾기 (Binary Lifting)
    for i in range(LOG-1, -1, -1):
        if parent[i][node1] != parent[i][node2]:
            node1 = parent[i][node1]
            node2 = parent[i][node2]
    
    return parent[0][node1]  # 찾은 LCA 바로 아래까지 왔으니 한 단계 위로

M = int(input())
for _ in range(M):
    node1, node2 = map(int, input().split())
    sys.stdout.write(str(find_lca(node1, node2)) + '\n')