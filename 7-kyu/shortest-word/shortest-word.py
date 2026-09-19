def find_short(s):
    s = s.split()
    low = s[0]
    for i in s:
        if len(i) < len(low):
            low = i
    return len(low)