import sys
input = sys.stdin.readline

char = [list(map(str, input().strip())) for _ in range(5)]
max_length = 0
# 가장 긴 문자열 리스트 길이 찾기
for i in range(5):
    if len(char[i]) >= max_length:
        max_length = len(char[i])

# 가장 긴 문자열 리스트보다 길이가 짧은 문자열 리스트에 0 추가
for i in range(5):
    if len(char[i]) < max_length:
        difference = max_length - len(char[i])
        for j in range(difference):
            char[i].append(0)

# 이차원 배열에 저장한 문자열 리스트를 가로로 순회하면서
for j in range(max_length):
    for i in range(5):
        if char[i][j] == 0:
            continue
        else:
            print(char[i][j], end='')