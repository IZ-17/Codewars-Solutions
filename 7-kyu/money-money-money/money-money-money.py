def calculate_years(principal, interest, tax, desired):
    count = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        count += 1
    return count