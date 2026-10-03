def get_num(n):
    return sum([1 if int(i) in [6, 9, 0] else 2 if int(i) == 8 else 0 for i in str(n)])