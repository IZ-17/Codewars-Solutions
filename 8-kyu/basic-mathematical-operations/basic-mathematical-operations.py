def basic_op(operator, value1, value2):
    if operator == "+": return value1 + value2
    if operator == "-": return value1 - value2
    if operator == "*": return value1 * value2
    if operator == "/" and value2 != 0: return value1 / value2