def n_sum(num, result = 0):
    if num <= 0:
        return result
    result += num % 10
    next = num // 10
    return n_sum(next, result)
    
print(n_sum(1234))