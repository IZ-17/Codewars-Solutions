def make_sentences(parts):
    text = " ".join(parts)
    text = text.replace(" ,", ",").replace(" .", ".")
    while ".." in text:
        text = text.replace("..", ".")
    if not text.endswith("."):
        text +=  "."
    return text