def is_isogram(word):
    if not isinstance(word, str):
        return False
    letters = [char for char in word.lower() if char.isalpha()]
    if not letters:
        return False
    first_char_count = letters.count(letters[0])
    for char in letters:
        if letters.count(char) != first_char_count:
            return False
    return True