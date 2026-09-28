def binary_array_to_number(arr):
    return sum([x * 2 ** index for index, x in enumerate(arr[::-1])])