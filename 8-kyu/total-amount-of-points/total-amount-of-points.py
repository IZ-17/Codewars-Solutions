def points(games):
    return sum(1 if num[0] == num[-1] else 3 if num[0] > num[-1] else 0 for num in games)