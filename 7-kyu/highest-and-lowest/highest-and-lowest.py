def high_and_low(numbers):
    num_list = [int(n) for n in numbers.split()]
    return (f"{max(num_list)} {min(num_list)}")