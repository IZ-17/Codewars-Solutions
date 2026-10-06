def first_non_consecutive(arr):
    for index in range(1, len(arr)):
        if arr[index] - arr[index - 1] != 1:
            return arr[index]
    return None