import sys
input = sys.stdin.readline

def main():
    def find_parent(parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 간선 클래스
    class Edge:
        def __init__(self, a, b, distance):
            self.a = a
            self.b = b
            self.distance = distance

    # 노드의 개수와 간선(union 연산)의 개수 입력 받기
    v, e = map(int, input().split())
    parent = [0] * (v + 1) # 부모 테이블 초기화

    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = [] 
    result = 0

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    # 모든 간선에 대한 정보 입력 받기
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append(Edge(a, b, cost))

    # 간선을 비용순으로 정렬
    edges.sort(key=lambda x: x.distance)

    # 간선을 하나씩 확인하며
    for edge in edges:
        a, b, cost = edge.a, edge.b, edge.distance
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    sys.stdout.write(str(result))

if __name__ == '__main__':
    main()