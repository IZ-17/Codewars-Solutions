def remove_smallest(numbers):
    if not numbers:
        return []
    dublicate = numbers.copy()
    dublicate.remove(min(dublicate))
    return dublicate