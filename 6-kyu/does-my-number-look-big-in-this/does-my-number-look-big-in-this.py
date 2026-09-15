def narcissistic( value ):
    summa = 0
    for i in str(value):
        summa += int(i) ** len(str(value))
    return summa == value