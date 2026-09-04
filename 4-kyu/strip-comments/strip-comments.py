def strip_comments(strng, markers):
    lines = strng.split("\n")
    result = []
    for line in lines:
        min_index = len(line)
        for marker in markers:
            if marker in line:
                idx = line.find(marker)
                if idx < min_index:
                    min_index = idx
        cleaned_line = line[:min_index].rstrip()
        result.append(cleaned_line)
    return "\n".join(result)