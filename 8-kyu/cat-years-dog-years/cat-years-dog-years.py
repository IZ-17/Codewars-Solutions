def human_years_cat_years_dog_years(human_years):
    if human_years == 2:
        return [2, 24, 24]
    if human_years  == 1:
        return [1, 15, 15]
    return [human_years, 24 + 4 * (human_years - 2), 24 + 5 * (human_years - 2)]