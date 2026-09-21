def tribonacci(signature, n):
    result = list(signature)
    while len(result) < n:
        next_val = sum(result[-3:])
        result.append(next_val)
    return result[:n]