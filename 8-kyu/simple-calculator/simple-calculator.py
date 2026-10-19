def calculator(x, y, op):
    if type(x) not in (int, float) or type(y) not in (int, float):
        return "unknown value"
    ops = {"+": x + y,
          "-": x - y,
          "*": x * y,
          "/": x / y}
    return ops.get(op, "unknown value")