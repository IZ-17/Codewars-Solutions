def is_pangram(st):
    return all(letter in st.lower() for letter in "abcdefgijklmnopqrstuvwxyz")