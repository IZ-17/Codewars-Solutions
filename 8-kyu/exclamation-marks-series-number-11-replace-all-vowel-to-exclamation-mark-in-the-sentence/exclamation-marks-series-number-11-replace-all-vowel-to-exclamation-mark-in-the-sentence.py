def replace_exclamation(st):
    return "".join("!" if x in "aeiouAEIOU" else x for x in st)