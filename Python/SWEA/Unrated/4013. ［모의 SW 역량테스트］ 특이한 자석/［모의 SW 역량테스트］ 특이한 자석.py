from collections import deque

def solve():
    T = int(input())
    for t in range(1, T+1):
        K = int(input())
        magnets = [deque(map(int, input().split())) for _ in range(4)]
        for _ in range(K):
            idx, d = map(int, input().split())
            idx -= 1  # 0-based index
            rotations = [0] * 4
            rotations[idx] = d

            # 오른쪽으로 회전 전파
            for i in range(idx, 3):
                if magnets[i][2] != magnets[i+1][6]:
                    rotations[i+1] = -rotations[i]
                else:
                    break

            # 왼쪽으로 회전 전파
            for i in range(idx, 0, -1):
                if magnets[i][6] != magnets[i-1][2]:
                    rotations[i-1] = -rotations[i]
                else:
                    break

            # 회전 적용
            for i in range(4):
                if rotations[i]:
                    magnets[i].rotate(rotations[i])

        # 점수 계산
        score = 0
        for i in range(4):
            if magnets[i][0] == 1:
                score += (1 << i)
        print(f"#{t} {score}")

if __name__ == "__main__":
    solve()