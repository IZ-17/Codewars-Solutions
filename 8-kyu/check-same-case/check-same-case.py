def same_case(a, b): 
    return 1 if (a.islower() and b.islower()) or (a.isupper() and b.isupper()) else -1 if not (a.isalpha() and b.isalpha()) else 0