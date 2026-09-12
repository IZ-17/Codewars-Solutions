def band_name_generator(name):
    return f"The {name.title()}" if name[0] != name[-1] else f"{name.title() + name[1:]}"