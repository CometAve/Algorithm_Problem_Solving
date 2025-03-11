def solution(a, b):
    comb_1 = int(str(a)+str(b))
    comb_2 = 2 * a * b
    if comb_1 > comb_2:
        return comb_1
    else:
        return comb_2