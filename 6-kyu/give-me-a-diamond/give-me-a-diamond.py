def diamond(n):
    if n < 1 or n % 2 ==0:
        return None
    result = []
    for i in range(n):
        distance = abs(n // 2 - i)
        spaces = " " * distance
        stars = "*" * (n - 2 * distance)
        result.append(spaces + stars + "\n")
    return "".join(result)