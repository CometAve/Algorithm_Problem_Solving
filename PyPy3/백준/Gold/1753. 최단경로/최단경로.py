import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

# 무한대를 의미하는 값으로 문제에서 주어진 최대 가중치보다 큰 값 사용
INF = int(1e9)

def main():
  V, E = map(int, input().split())
  K = int(input())
  # 그래프 초기화: 1번 노드부터 사용하기 위해 V+1 크기의 리스트로 만듦
  graph = [[] for _ in range(V+1)]
  # 최단거리 테이블을 INF로 초기화
  distance = [INF] * (V+1)

  # 각 간선 정보를 입력 받아 그래프에 추가
  for _ in range(E):
      u, v, w = map(int, input().split())
      graph[u].append((v, w))
  

  def dijkstra(start, graph, distance):
      # 우선순위 큐 생성: (거리, 노드) 튜플을 저장합니다.
      q = []
      # 시작 노드의 거리를 0으로 설정하고 큐에 추가합니다.
      heapq.heappush(q, (0, start))
      distance[start] = 0

      while q:
          # 가장 짧은 거리를 가진 노드 추출
          dist, now = heapq.heappop(q)
          # 이미 처리된 노드라면 무시
          if distance[now] < dist:
              continue
          # 현재 노드와 인접한 모든 노드를 검사
          for next_node, weight in graph[now]:
              # 현재 노드를 거쳐 다음 노드까지의 비용 계산
              cost = dist + weight
              # 계산한 비용이 기존 최단거리보다 짧으면 갱신
              if cost < distance[next_node]:
                  distance[next_node] = cost
                  # 갱신된 거리와 함께 다음 노드를 큐에 추가
                  heapq.heappush(q, (cost, next_node))

  dijkstra(K, graph, distance)
  
  # 각 노드까지의 최단 거리를 출력. 도달할 수 없는 경우 INF 출력
  for i in range(1, V+1):
      if distance[i] == INF:
          print("INF\n")
      else:
          print(f"{distance[i]}\n")

if __name__ == '__main__':
    main()