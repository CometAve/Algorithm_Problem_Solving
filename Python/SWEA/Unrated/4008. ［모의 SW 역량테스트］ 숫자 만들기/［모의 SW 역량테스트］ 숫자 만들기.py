def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        op = list(map(int, input().split()))
        num = list(map(int, input().split()))
        max_val = -100000000
        min_val = 100000000
        def perm(idx, result):
            nonlocal max_val, min_val
            if idx == N-1:
                max_val = max(max_val, result)
                min_val = min(min_val, result)
                return
            for i in range(4):
                if op[i] > 0:
                    op[i] -= 1
                    if i == 0:
                        perm(idx+1, result + num[idx+1])
                    elif i == 1:
                        perm(idx+1, result - num[idx+1])
                    elif i == 2:
                        perm(idx+1, result * num[idx+1])
                    elif i == 3:
                        perm(idx+1, int(result / num[idx+1]))
                    op[i] += 1
        perm(0, num[0])
        print(f'#{tc} {max_val - min_val}')

if __name__ == "__main__":
    main()