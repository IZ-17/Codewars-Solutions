def persistence(n):
    steps = 0
    while n >= 10:
        result = 1
        for i in str(n):
            result *= int(i)
        n = result
        steps += 1
    return steps