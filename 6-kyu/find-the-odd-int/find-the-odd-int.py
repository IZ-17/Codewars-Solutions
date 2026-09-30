def find_it(seq):
    return int([a for a in seq if seq.count(a) % 2 != 0][0])