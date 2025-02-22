import sys
input = sys.stdin.readline


def dfs(node, graph, visited):
    visited[node] = True # 현재 노드 방문 표시
    count = 1 # 헷갈리니 자기 자신부터 카운트 (나중에 자기 자신 뺌)
              # 재귀사용할 때 본인 포함해서 계산해야 정확하기 때문

    # 현재 노드와 연결된 모든 노드를 확인
    for next_node in graph[node]:
        # 연결된 노드를 방문 안 했으면
        if not visited[next_node]:
            # 연결된 노드와 연결된 또 다른 노드들을 전부 카운트
            count += dfs(next_node, graph, visited)
    return count

# N : 전체 학생 수, M : 비교한 횟수
N, M = map(int, input().split())

# 두 가지 그래프 생성:
# 1. 정방향 그래프: A -> B (A가 B보다 키가 작음)
# 2. 역방향 그래프: B -> A (B가 A보다 키가 큼)
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    V, E = map(int, input().split())
    graph[V].append(E)
    reverse_graph[E].append(V)

result = 0 # 순서를 확실히 알 수 있는 학생 수를 저장할 변수

# 각 학생에 대해
for student in range(1, N + 1):
    # 1. 해당 학생보다 키가 큰 학생들의 개수를 계산 (정방향)
    forward_visited = [False] * (N + 1)
    count_taller = dfs(student, graph, forward_visited) - 1 # 자기 자신은 빼주기

    # 2. 해당 학생보다 키가 작은 학생들의 개수를 계산 (역방향)
    backward_visited = [False] * (N + 1)
    count_shorter = dfs(student, reverse_graph, backward_visited) - 1

    # 두 값의 합이 전체 학생 수 - 1과 같다면,
    # 즉, student와 비교 가능한 모든 노드와 연결되어 있음을 의미
    if count_taller + count_shorter == N - 1:
        result += 1

print(result)