def calculate_age(year_of_birth, current_year):
    if year_of_birth < current_year:
        if current_year - year_of_birth == 1:
            return f"You are {current_year - year_of_birth} year old."
        else:
            return f"You are {current_year - year_of_birth} years old."
    if year_of_birth > current_year:
         if year_of_birth - current_year == 1:
            return f"You will be born in {year_of_birth - current_year} year."
         else:
            return f"You will be born in {year_of_birth - current_year} years."
    else: return "You were born this very year!"