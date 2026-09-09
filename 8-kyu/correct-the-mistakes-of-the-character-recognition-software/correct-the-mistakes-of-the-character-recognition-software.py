def correct(s):
    alpha = {
        "0": "O",
        "1": "I",
        "5": "S"
    }
    return "".join(x if not x.isdigit() else alpha[x] for x in s)