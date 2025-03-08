# 최소 힙(Min Heap) 구현 - 항상 가장 작은 값을 빠르게 찾을 수 있는 완전 이진 트리 자료구조
# 힙은 배열로 표현할 수 있으며, 부모-자식 관계는 인덱스로 계산됨
import sys
input = sys.stdin.readline
n = int(input())  # 수행할 연산의 개수
heap = []  # 힙을 저장할 배열 - 완전 이진 트리 형태로 데이터가 저장됨

def insert(x):
    # 새 값은 일단 힙의 마지막에 추가 (완전 이진 트리의 마지막 위치)
    heap.append(x)
    # 추가된 값의 인덱스 - 힙의 마지막 위치에서 시작
    i = len(heap) - 1
    
    # 힙 속성 복구 과정 (상향식) - 부모보다 작은 값이면 위로 올라감
    while i > 0:
        # 부모 노드의 인덱스 계산: 완전 이진 트리에서 부모 = (자식 인덱스-1) // 2
        parent = (i - 1) // 2
        # 최소 힙 속성 점검 - 부모가 더 크면 위치 교환 필요
        if heap[parent] > heap[i]:
            # 부모와 현재 노드 위치 교환 (swap)
            heap[parent], heap[i] = heap[i], heap[parent]
            # 이제 부모 위치로 이동해서 계속 검사
            i = parent
        else:
            # 최소 힙 속성 만족 - 더 이상 상향 이동 불필요
            break

def delete():
    # 힙이 비었다면 0 출력 후 종료
    if not heap:
        print(0)
        return
    
    # 최소값(루트) 출력 - 최소 힙의 루트는 항상 배열의 첫 요소
    print(heap[0])
    
    # 힙의 마지막 요소를 루트로 이동 (임시로 힙 속성 깨짐)
    heap[0] = heap[-1]
    # 마지막 요소 제거 (이미 루트로 복사했으므로)
    heap.pop()
    
    # 힙 속성 복구 과정 (하향식) - 루트부터 시작
    i = 0
    # 왼쪽 자식이 존재하는 동안 계속 (완전 이진 트리에서 왼쪽 자식 = 부모 인덱스*2 + 1)
    while i * 2 + 1 < len(heap):
        # 왼쪽 자식 인덱스 계산
        left = i * 2 + 1
        # 오른쪽 자식 인덱스 계산
        right = i * 2 + 2
        
        # 두 자식 중 더 작은 값을 가진 자식 선택
        # 오른쪽 자식이 존재하고, 오른쪽이 왼쪽보다 작으면 오른쪽 선택
        if right < len(heap) and heap[right] < heap[left]:
            left = right  # left 변수에 더 작은 자식의 인덱스 저장
        
        # 현재 노드가 선택된 자식보다 크면 교환 필요
        if heap[i] > heap[left]:
            # 현재 노드와 선택된 자식 교환 (swap)
            heap[i], heap[left] = heap[left], heap[i]
            # 이제 교환된 자식 위치로 이동하여 계속 검사
            i = left
        else:
            # 최소 힙 속성 만족 - 더 이상 하향 이동 불필요
            break

for _ in range(n):
    x = int(input())
    if x == 0:  # 0이면 최소값 삭제 후 출력
        delete()
    else:  # 자연수면 힙에 값 추가
        insert(x)