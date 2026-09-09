def count(s):
    dct = dict()
    x = set(s)
    for i in x:
        dct[i] = s.count(i)
    return dct