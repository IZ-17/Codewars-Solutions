def find_needle(haystack):
    for index, item in enumerate(haystack):
        if item == "needle": return f"found the needle at position {index}"