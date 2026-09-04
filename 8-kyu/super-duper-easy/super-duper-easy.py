def problem(a):
    return a * 50 + 6 if isinstance(a, (int, float)) and type(a) is not bool else "Error"