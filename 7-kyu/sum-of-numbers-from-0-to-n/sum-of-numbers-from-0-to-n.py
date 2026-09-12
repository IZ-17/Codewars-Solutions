def show_sequence(n):
    return f"{'+'.join([str(num) for num in range(n + 1)])} = {sum(num for num in range(n + 1))}" if n > 0 else f"{n}=0" if n == 0 else f"{n}<0"