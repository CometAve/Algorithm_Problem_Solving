# 다른 풀이
T = int(input())

# 리스트로 결과를 저장하고 마지막에 한 번에 출력하면
# 출력 속도가 빨라진다고 함
# 만약 출력 순서가 중요하지 않으면 이 방법을 사용
result = []

for tc in range(1, T+1):
    N, M = map(int, input().split())
    if M % 2**N == 2**N - 1:
        result.append(f'#{tc} ON')
    else:
        result.append(f'#{tc} OFF')

print('\n'.join(result))