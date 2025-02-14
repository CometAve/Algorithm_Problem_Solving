import sys
input = sys.stdin.readline

def get_max_length(lan, N):
    start = 1
    end = max(lan)
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in lan:
            count += i // mid
        if count >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
max_length = get_max_length(lan, N)
print(max_length)