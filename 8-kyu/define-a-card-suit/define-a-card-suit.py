def define_suit(card):
    suits = {
        'C': 'clubs',
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades'
    }
    return suits[card[-1]]