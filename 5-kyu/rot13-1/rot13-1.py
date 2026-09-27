def rot13(message):
    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_rot = "nopqrstuvwxyzabcdefghijklm"
    trans = str.maketrans(abc + abc.upper(), abc_rot + abc_rot.upper())
    return message.translate(trans)