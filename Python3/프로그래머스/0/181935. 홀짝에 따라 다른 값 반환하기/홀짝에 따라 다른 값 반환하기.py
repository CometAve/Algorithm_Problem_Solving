def solution(n):
    answer = 0
    # 홀수인지 짝수인지 판별
    # 만약 홀수라면
    if n % 2 != 0:
        # n을 포함시키기 위해 + 1
        for i in range(n + 1):
            # 홀수만 더함
            if i % 2 != 0:
                answer += i
        else:
             return answer  
    # 짝수라면
    else:
        for i in range(n + 1):
            # 짝수의 제곱의 합
            if i % 2 == 0:
                answer += i*i
        else:
            return answer
