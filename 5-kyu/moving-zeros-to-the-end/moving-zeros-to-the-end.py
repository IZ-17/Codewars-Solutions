def move_zeros(lst):
    zeros = []
    other = []
    for i in lst:
        if i == 0:
            zeros.append(i)
        else:
            other.append(i)
    return other + zeros