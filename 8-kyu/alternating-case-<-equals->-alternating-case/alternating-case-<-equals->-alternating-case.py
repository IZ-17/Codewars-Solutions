def to_alternating_case(string):
    result = ""
    for i in string:
        if i == i.lower():
            result += i.upper()
        else:
            result += i.lower()
    return result