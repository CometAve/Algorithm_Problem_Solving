T = 10

def is_valid_bracket(brackets):
    brackets = list(brackets)
    type_of_brackets = ['(', ')', '[', ']', '{', '}', '<', '>']
    count_list = [0] * 8
    for bracket in brackets:
        count_list[type_of_brackets.index(bracket)] += 1

    if count_list[0] != count_list[1] or count_list[2] != count_list[3] or count_list[4] != count_list[5] or count_list[6] != count_list[7]:
        return 0
    else:
        return 1

for tc in range(1, T + 1):
    N = int(input())
    brackets = input()
    print(f'#{tc} {is_valid_bracket(brackets)}')