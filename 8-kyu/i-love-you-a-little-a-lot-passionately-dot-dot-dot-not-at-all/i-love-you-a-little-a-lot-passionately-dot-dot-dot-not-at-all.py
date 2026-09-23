def how_much_i_love_you(nb_petals):
    answers = {1:"I love you",
    2:"a little",
    3:"a lot",
    4:"passionately",
    5:"madly",
    0:"not at all"}
    return answers[nb_petals % 6]