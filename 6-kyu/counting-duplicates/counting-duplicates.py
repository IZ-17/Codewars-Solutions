def duplicate_count(text):
    result = [x for x in set(text.lower()) if text.lower().count(x) > 1]
    return len(result)