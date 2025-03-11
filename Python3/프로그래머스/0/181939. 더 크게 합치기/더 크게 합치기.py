def solution(a, b):
    answer = 0
    ex_1 = int(str(a) + str(b))
    ex_2 = int(str(b) + str(a))
    
    if ex_1 > ex_2:
        answer = ex_1
        return answer
    else:
        answer = ex_2
        return answer