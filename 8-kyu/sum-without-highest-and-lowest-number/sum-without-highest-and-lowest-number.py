def sum_array(arr):
    return sum(sorted(arr)[1:len(arr) - 1]) if arr else 0