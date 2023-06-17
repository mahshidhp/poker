from Card import ranks, Card
from utils import Colors


class PokerCalculator:
    def __init__(self, cards):
        self.cards = cards

        # stores count of every rank
        self.cards_count = [0 for _ in range(13)]

        # empty 4 * 13 table determining presence of each card
        self.cards_table = [[False for _ in range(13)] for __ in range(4)]

        self.calc_cards_count()
        self.calc_cards_table()

    def calc_cards_count(self):
        for card in self.cards:
            self.cards_count[card.rank] += 1

    def calc_cards_table(self):
        for card in self.cards:
            self.cards_table[card.suit][card.rank] = True

    def calc_best_options(self):
        self.calc_royal_flush()
        self.calc_straight_flush()
        # self.calc_four_of_a_kind()
        # self.calc_full_house()
        # self.calc_flush()
        self.calc_straight()
        # self.calc_three_of_a_kind()
        # self.calc_two_pairs()
        # self.calc_pair()
        # self.calc_high_card()


    def calc_royal_flush(self):
        result = []
        for suit in range(4):
            matching_cards = [Card(suit, rank) for rank in range(8, 13) if self.cards_table[suit][rank]]
            missing_cards = [Card(suit, rank) for rank in range(8, 13) if not self.cards_table[suit][rank]]
            if len(matching_cards) >= 3:
                result.append((matching_cards, missing_cards))
        self.print_result("Royal flush", result)

    def calc_straight_flush(self):
        result = []
        for suit in range(4):
            for starting_rank in range(9):
                matching_cards = [Card(suit, rank) for rank in range(starting_rank, starting_rank+5) if self.cards_table[suit][rank]]
                missing_cards = [Card(suit, rank) for rank in range(starting_rank, starting_rank+5) if not self.cards_table[suit][rank]]
                if len(matching_cards) >= 3:
                    result.append((matching_cards, missing_cards))
        self.print_result("Straight flush", result)

    # def calc_four_of_a_kind(self):
    #     result = []
    #     self.print_result("Four of a kind", result)

    # def calc_full_house(self):
    #     result = []
    #     self.print_result("Full house", result)

    # def calc_flush(self):
    #     result = []
    #     self.print_result("Flush", result)

    def calc_straight(self):
        result = []
        for starting_rank in range(9):
            matching_cards = [ranks[rank] for rank in range(starting_rank, starting_rank+5) if self.cards_count[rank]>0]
            missing_cards = [ranks[rank] for rank in range(starting_rank, starting_rank+5) if self.cards_count[rank]==0]
            if len(matching_cards) >= 3:
                result.append((matching_cards, missing_cards))
        self.print_result("Straight", result)

    # def calc_three_of_a_kind(self):
    #     result = []
    #     self.print_result("Three of a kind", result)

    # def calc_two_pairs(self):
    #     result = []
    #     self.print_result("Two pairs", result)

    # def calc_pair(self):
    #     result = []
    #     self.print_result("Pair", result)

    # def calc_high_card(self):
    #     result = []
    #     self.print_result("High card", result)

    def print_result(self, title, results):
        print(Colors.OKCYAN + "--------------------------------" + Colors.ENDC)
        print(Colors.OKCYAN + title + Colors.ENDC)
        for present, missing in results:
            print(f"{present}, missing: {missing}")
