# 16진수 숫자가 적혀 있는 보물상자
# 자물쇠를 돌리면 숫자들이 하나씩 밀려나며 가장 마지막에 있는 숫자는 맨 앞으로 이동한다.
# 회전을 3번하면 다시 처음 상태로 돌아온다.
# 회전하면서 생성된 16진수를 저장하고 내림차순 정렬 후 K번째로 큰 수를 출력하라.
# 중복된 수는 하나로 취급한다.

# 설계
# 16진수를 10진수로 변환하는 함수를 만든다.
# 회전을 ranage(N//4)으로 반복하면서 16진수를 생성한다
# 회전하면 배열에 3개씩 끊어서 16진수를 확인하고,
# 중복되지 않는 16진수이면 저장.
# 회전이 끝나면 내림차순 후 K번째 수를 출력한다.
# N은 4의 배수이므로 N//4로 나누어서 16진수를 생성한다.
# N개의 숫자는 0이상 F이하이므로 16진수로 변환하면 0이상 15이하이다.

def hex_to_dec(hex):
    dec = 0
    for i in range(len(hex)):
        dec += int(hex[i], 16) * 16**(len(hex)-i-1)
    return dec

def solve():
    T = int(input())
    for tc in range(1, T+1):
        N, K = map(int, input().split())
        nums = list(input())
        hexes = []
        for _ in range(N//4):
            for i in range(0, N, N//4):
                if ''.join(nums[i:i+N//4]) in hexes:
                    continue
                else:
                    hexes.append(''.join(nums[i:i+N//4]))
            nums = nums[-1] + ''.join(nums[:-1])
        hexes = sorted(hexes, reverse=True)
        print(f'#{tc} {hex_to_dec(hexes[K-1])}')

if __name__ == '__main__':
    solve()