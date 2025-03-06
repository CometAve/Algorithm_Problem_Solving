import sys
input = sys.stdin.readline

tar = int(input())
result = []

while tar > 0:
    result.append(tar % 2)
    tar = tar // 2
    
result.reverse()
ans = ''.join(map(str, result))
print(ans)