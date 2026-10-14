def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("n must be between 0 and 12")
    if n <= 1:
        return 1
    return n * factorial(n - 1)