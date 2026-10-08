def highest_rank(arr):
    return max(set(arr),key = lambda x: (arr.count(x), x))