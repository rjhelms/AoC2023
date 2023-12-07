from time import perf_counter
from collections import Counter

IN_FILE = "07/input.txt"

# hand scores:
# high card: 0
# one pair: 1
# two pair: 2
# three of a kind: 3
# full house: 4
# four of a kind: 5
# five of a kind: 6


class Hand:
    def __init__(self, cards: str, bid: int) -> None:
        self.cards = cards
        self.bid = bid

        # cast letters to A-E so can use string

        self.cards = (
            self.cards.replace("A", "E")
            .replace("K", "D")
            .replace("Q", "C")
            .replace("J", "1")  # replace joker with 1 (so is bottom of sort)
            .replace("T", "A")
        )

    def get_type(self):
        joker_count = self.cards.count("1")

        # special case - if there's 5 jokers, test_cards is empty string so further logic won't work
        if joker_count == 5:
            return 6

        test_cards = self.cards.replace("1", "")
        counter = Counter(test_cards).most_common()

        if counter[0][1] + joker_count == 5:  # five of a kind
            return 6
        if counter[0][1] + joker_count == 4:  # four of a kind
            return 5
        if counter[0][1] + joker_count == 3:  # 3 of one card...
            if counter[1][1] == 2:  # full house
                return 4
            else:  # three of a kind
                return 3
        if counter[0][1] + joker_count == 2:  # two of one card
            if counter[1][1] == 2:  # two pair
                return 2
            else:  # one pair
                return 1
        return 0  # high card

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if self.get_type() == other.get_type():
            return self.cards < other.cards
        else:
            return self.get_type() < other.get_type()


if __name__ == "__main__":
    start_time = perf_counter()

    hands: list[Hand] = []

    with open(IN_FILE) as f:
        for row in f:
            row = row.strip().split()
            new_hand = Hand(row[0], int(row[1]))
            hands.append(new_hand)

    hands.sort()

    score = 0

    rank = 1
    for hand in hands:
        score += rank * hand.bid
        rank += 1

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
