import sys
input = sys.stdin.readline

n = int(input())
n_list = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
for m in m_list:
    print(1 if m in n_list else 0)