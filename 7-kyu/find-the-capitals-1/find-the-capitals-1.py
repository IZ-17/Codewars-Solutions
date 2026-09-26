def capitals(word):
    return [index for index, letter in enumerate(word) if letter.isupper()]