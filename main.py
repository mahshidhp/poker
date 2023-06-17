from PokerCalculator import PokerCalculator
from Card import Card, suit_symbols, ranks


def parse_input_cards(club_ranks, spade_ranks, heart_ranks, diamond_ranks):
    cards = []
    cards += [Card(0, ranks.index(rank)) for rank in club_ranks]
    cards += [Card(1, ranks.index(rank)) for rank in heart_ranks]
    cards += [Card(2, ranks.index(rank)) for rank in diamond_ranks]
    cards += [Card(3, ranks.index(rank)) for rank in spade_ranks]
    return cards

if __name__ == "__main__":
    print("Ranks = {2 3 4 5 6 7 8 9 10 j q k a}")
    print(f"Please enter club({suit_symbols[0]}) ranks seperated by space:")
    club_ranks = input().split()
    print(f"Please enter heart({suit_symbols[1]}) ranks seperated by space:")
    heart_ranks = input().split()
    print(f"Please enter diamond({suit_symbols[2]}) ranks seperated by space:")
    diamond_ranks = input().split()
    print(f"Please enter spade({suit_symbols[3]}) ranks seperated by space:")
    spade_ranks = input().split()

    cards = parse_input_cards(club_ranks, spade_ranks, heart_ranks, diamond_ranks)

    poker_calculator = PokerCalculator(cards)
    poker_calculator.calc_best_options()
