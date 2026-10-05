def vowel_indices(word):
    return [index for index, letter in enumerate(word, start = 1) if letter.lower() in "aeiouy"]