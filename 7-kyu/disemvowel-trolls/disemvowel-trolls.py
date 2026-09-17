def disemvowel(string_):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    result = [char for char in string_ if char not in vowels] 
    return "".join(result)