def tower_builder(n):
    result = []
    for i in range(n): 
         result. append(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i - 1))
    return result