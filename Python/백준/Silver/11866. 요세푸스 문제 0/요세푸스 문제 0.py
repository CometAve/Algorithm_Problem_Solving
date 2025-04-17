from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N + 1))

ans = []
while queue:
    cnt = 1
    while cnt < K:
        tmp = queue.popleft()
        queue.append(tmp)
        cnt += 1
    tmp = queue.popleft()
    ans.append(tmp)

print("<", end="")
print(*ans, sep=", ", end="")
print(">")
