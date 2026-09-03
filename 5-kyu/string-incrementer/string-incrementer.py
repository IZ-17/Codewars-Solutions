def increment_string(string):
    strn = string.rstrip('0123456789')
    t = string[len(strn):]
    if not t: 
        return string + "1"
    return strn + str(int(t) + 1).zfill(len(t))