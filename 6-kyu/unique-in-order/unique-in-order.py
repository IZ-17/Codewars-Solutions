def unique_in_order(sequence):
    result = []
    for i in sequence:
        if not result or i != result[-1]:
            result.append(i)
    return result