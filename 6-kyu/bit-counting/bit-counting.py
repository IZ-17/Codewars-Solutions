def count_bits(n):
    count = 0
    clean_bin = bin(n)[2:]
    for i in str(clean_bin):
        if i == "1":
            count += 1
    return count