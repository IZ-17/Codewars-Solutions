def cube_checker(volume, side):
    return side ** 3 == volume if side > 0 and volume > 0 else False