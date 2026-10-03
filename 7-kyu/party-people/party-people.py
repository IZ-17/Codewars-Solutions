def party_people(lst):
    lst.sort()
    while lst and len(lst) < lst[-1]:
        lst.pop()
    return len(lst)