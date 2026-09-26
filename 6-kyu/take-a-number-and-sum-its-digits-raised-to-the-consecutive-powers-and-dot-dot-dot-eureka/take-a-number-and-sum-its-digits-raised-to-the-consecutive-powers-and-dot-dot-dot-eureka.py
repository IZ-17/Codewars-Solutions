def sum_dig_pow(a, b):
    return [x for x in range(a, b + 1) if sum(int(d) ** (index + 1) for index, d in enumerate(str(x))) == x]