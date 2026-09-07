def solution(s):
    return "".join(i if i == i.lower() else f" {i}" for i in s)