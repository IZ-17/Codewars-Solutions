def queue_time(customers, n):
    if n >= len(customers):
        if not customers:
            return 0
        return max(customers)
    tills = [0] * n
    for time in customers:
        min_time = min(tills)
        min_index = tills.index(min_time)
        tills[min_index] += time   
    return max(tills)