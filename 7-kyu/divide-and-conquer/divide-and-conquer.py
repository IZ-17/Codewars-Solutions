def div_con(x):
    return sum(num if isinstance(num, int) else -int(num) for num in x)