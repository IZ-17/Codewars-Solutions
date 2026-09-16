def numbers_of_letters(n):
    NUM_WORDS = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    result = []
    while True:
        word = "".join(NUM_WORDS[int(i)] for i in str(n))
        result.append(word)
        if len(word) == n:
            break
        n = len(word)
    return result