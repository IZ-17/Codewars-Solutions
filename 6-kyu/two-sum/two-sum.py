def two_sum(numbers, target):
    seen = {}
    for index, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return (seen[complement], index)
        else:
            seen[num] = index