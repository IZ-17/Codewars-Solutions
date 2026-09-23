def order(sentence):
    if not sentence:
        return ""
    return " ".join(sorted(sentence.split(), key = lambda word: sorted(word)))