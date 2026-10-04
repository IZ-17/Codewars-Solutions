def check_valid_tr_number(number):
    number = str(number)
    if not number.isdigit() or len(number) != 11 or number[0] == "0":
        return False
    odd_sum = int(number[0]) + int(number[2]) + int(number[4]) + int(number[6]) + int(number[8])
    even_sum = int(number[1]) + int(number[3]) + int(number[5]) + int(number[7])
    rule_10 = (odd_sum * 7 - even_sum) % 10 == int(number[9])
    rule_11 = (odd_sum + even_sum + int(number[9])) % 10 == int(number[10])
    return rule_10 and rule_11