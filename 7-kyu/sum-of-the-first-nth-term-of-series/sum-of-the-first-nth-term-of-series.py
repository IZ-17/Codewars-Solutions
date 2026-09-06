def series_sum(n):
    return f"{sum(1 / (1 + 3 * (x - 1)) for x in range(1, n + 1)):.2f}"