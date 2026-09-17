def remove(st):
    return " ".join(word.rstrip("!") for word in st.split(" "))