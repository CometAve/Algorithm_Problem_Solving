def rotate(magnet, direction):
    # 시계 방향이면 마지막 원소를 앞으로, 반시계는 첫 원소를 뒤로 이동
    if direction == 1:
        return magnet[-1:] + magnet[:-1]
    elif direction == -1:
        return magnet[1:] + magnet[:1]
    return magnet

def solve():
    T = int(input())
    for t in range(1, T+1):
        K = int(input())
        magnets = [list(map(int, input().split())) for _ in range(4)]
        for _ in range(K):
            idx, d = map(int, input().split())
            idx -= 1  # 인덱스 0부터 시작
            # 각 자석의 회전 방향 저장, 0이면 회전하지 않음
            rotations = [0] * 4
            rotations[idx] = d
            
            # 오른쪽 자석으로 전파
            for i in range(idx, 3):
                if magnets[i][2] != magnets[i+1][6]:
                    rotations[i+1] = -rotations[i]
                else:
                    break
            
            # 왼쪽 자석으로 전파
            for i in range(idx, 0, -1):
                if magnets[i][6] != magnets[i-1][2]:
                    rotations[i-1] = -rotations[i]
                else:
                    break
            
            # 회전 적용
            for i in range(4):
                if rotations[i]:
                    magnets[i] = rotate(magnets[i], rotations[i])
        
        # 점수 계산: 자석 1, 2, 3, 4는 각각 1, 2, 4, 8점
        score = sum(magnets[i][0] * (1 << i) for i in range(4))
        print(f"#{t} {score}")

if __name__ == "__main__":
    solve()