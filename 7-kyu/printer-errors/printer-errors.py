def printer_error(s):
    result = 0
    for x in s:
        if x not in "abcdefghijklm":
            result += 1
    return f"{result}/{len(s)}"