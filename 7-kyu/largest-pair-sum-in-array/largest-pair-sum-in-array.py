def largest_pair_sum(numbers): 
    return sum(sorted(numbers, reverse = True)[0:2])