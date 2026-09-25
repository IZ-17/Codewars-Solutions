def find_next_square(sq):
    return (sq ** 0.5 + 1) ** 2 if sq ** 0.5 % 1 == 0 else -1