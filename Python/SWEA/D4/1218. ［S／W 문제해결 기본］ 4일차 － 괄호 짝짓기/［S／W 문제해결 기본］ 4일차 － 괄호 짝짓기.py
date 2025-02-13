T = 10

# stack으로 풀어보기
def remove_if_bracket_matched(string):
    bracket_pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
    stack = []
    brackets = list(string)
    for bracket in brackets:
        stack.append(bracket)
        if len(stack) > 1:
            if stack[-2] in bracket_pairs.keys() and stack[-1] == bracket_pairs[stack[-2]]:
                stack.pop()
                stack.pop()
            else:
                continue
    return 1 if len(stack) == 0 else 0

for tc in range(1, T + 1):
    N = int(input())
    brackets = input()
    print(f'#{tc} {remove_if_bracket_matched(brackets)}')