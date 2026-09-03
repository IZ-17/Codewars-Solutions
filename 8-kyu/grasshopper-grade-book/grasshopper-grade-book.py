def get_grade(s1, s2, s3):
    total = (s1 + s2 + s3) // 3
    return "F" if total < 60 else "D" if total < 70 else "C" if total < 80 else "B" if total < 90 else "A" 