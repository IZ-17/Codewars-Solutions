def update_light(current):
    if current == "yellow":
        return "red"
    if current == "red":
        return "green"
    return "yellow"