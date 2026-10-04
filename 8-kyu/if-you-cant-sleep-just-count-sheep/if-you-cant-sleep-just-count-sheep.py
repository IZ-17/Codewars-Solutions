def count_sheep(n):
    if not n:
        return ""
    return "".join(f"{i} sheep..." for i in range(1, n + 1))