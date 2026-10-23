def capitalize(s):
    s1 = "".join(c.upper() if index % 2 == 0 else c for index, c in enumerate(s))
    return [s1, s1.swapcase()]