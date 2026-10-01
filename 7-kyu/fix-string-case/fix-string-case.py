def solve(s):
    return s.lower() if len([x for x in s if x == x.lower()]) >= len(s) / 2 else s.upper()