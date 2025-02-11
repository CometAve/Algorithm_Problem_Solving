T = int(input())

for tc in range(1, T + 1):
    word = input()

    print(f'#{tc}', end=' ')
    if word == word[::-1]:
        print(1)
    else:
        print(0)