def star(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        pattern = star(n//3)
        result = []
        for i in range(n):
            if i // (n//3) == 1:
                result.append(pattern[i % (n//3)] + ' '*(n//3) + pattern[i % (n//3)])
            else:
                result.append(pattern[i % (n//3)]*3)
        return result
    
n = int(input())
print('\n'.join(star(n)))