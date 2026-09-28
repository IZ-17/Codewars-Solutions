def title_case(title, minor_words=''):
    if not title:
        return ""
    words = title.lower().split()
    minor_list = minor_words.lower().split()
    result = [words[0].capitalize()]
    for word in words[1:]:
        if word in minor_list:
            result.append(word)
        else:
            result.append(word.capitalize())
    return " ".join(result)
    