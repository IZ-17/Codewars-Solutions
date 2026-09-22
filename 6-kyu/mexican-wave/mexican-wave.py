def wave(people):
    result = []
    for index, i in enumerate(people):
        if i.isspace():
            continue
        wave_str = people[:index] + i.upper() + people[index + 1:]
        result.append(wave_str)
    return result