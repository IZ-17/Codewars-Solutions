def dig_pow(n, p):
    result = 0
    i = 0
    for x in str(n):
        result += int(x) ** (p + i)
        i += 1
    return result // n if result % n == 0 else -1