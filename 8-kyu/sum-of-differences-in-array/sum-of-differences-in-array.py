def sum_of_differences(arr):
    if not arr:
        return 0
    arr.sort(reverse = True)
    return sum(arr[i] - arr[i + 1] for i in range(len(arr) - 1))