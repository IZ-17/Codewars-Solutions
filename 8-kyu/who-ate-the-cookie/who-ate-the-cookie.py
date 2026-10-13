def cookie(x):
    if type(x) is bool:
        name = "the dog"
    else:
        name = {
            str: "Zach",
            int: "Monica",
            float: "Monica"
        }.get(type(x),"the dog")
    return f"Who ate the last cookie? It was {name}!"