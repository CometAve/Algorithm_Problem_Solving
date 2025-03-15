def min_palindrome_partitions(s):
    n = len(s)
    
    # 팰린드롬 판별을 위한 DP 테이블
    # is_palindrome[i][j]: s[i:j+1]이 팰린드롬인지 여부
    is_palindrome = [[False] * n for _ in range(n)]
    
    # 길이 1인 문자열은 항상 팰린드롬
    for i in range(n):
        is_palindrome[i][i] = True
    
    # 길이 2인 문자열 체크
    for i in range(n-1):
        if s[i] == s[i+1]:
            is_palindrome[i][i+1] = True
    
    # 길이 3 이상인 문자열 체크
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            # 양 끝이 같고, 내부가 팰린드롬이면 팰린드롬
            if s[i] == s[j] and is_palindrome[i+1][j-1]:
                is_palindrome[i][j] = True
    
    # dp[i]: s[0:i+1]에 대한 최소 팰린드롬 분할 개수
    dp = [float('inf')] * n
    
    for i in range(n):
        # 처음부터 i까지가 하나의 팰린드롬이면 분할 개수는 1
        if is_palindrome[0][i]:
            dp[i] = 1
        else:
            # j를 기준으로 분할했을 때의 최소 분할 개수 찾기
            for j in range(i):
                if is_palindrome[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n-1]

# 입력 처리
s = input().strip()
print(min_palindrome_partitions(s))
