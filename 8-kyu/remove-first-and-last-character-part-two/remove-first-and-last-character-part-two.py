def array(string):
    elements = string.split(",")
    if len(elements) < 3:
        return None
    return " ".join(elements[1:-1])