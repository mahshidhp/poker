from utils import Colors

ranks = [
    '2', '3', '4', '5', '6',
    '7', '8', '9', '10',
    'j', 'q', 'k', 'a'
]

suit_symbols = [
    "\u2663", #CLUB
    "\u2665", #HEART
    "\u2666", #DIAMOND
    "\u2660"  #SPADE
]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        str = ranks[self.rank] + suit_symbols[self.suit]
        if self.suit == 1 or self.suit == 2:
            return Colors.FAIL + str + Colors.ENDC
        return str

    def __repr__(self):
        return self.__str__()
