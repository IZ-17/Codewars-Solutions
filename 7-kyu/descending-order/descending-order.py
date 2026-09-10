def descending_order(num):
    result = sorted(str(num), reverse = True)
    return int("".join(result))