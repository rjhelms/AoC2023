from time import perf_counter

IN_FILE = "04/input.txt"


class Card:
    def __init__(self, id: int, winners: list) -> None:
        self.id = id
        self.winners = winners

    def get_bonus_card_ids(self) -> list:
        start = self.id + 1
        stop = start + self.winners
        return range(start, stop)


if __name__ == "__main__":
    start_time = perf_counter()

    score = 0

    card_open_list: list[Card] = []
    card_closed_list: list[Card] = []
    card_dict: dict[Card] = {}

    with open(IN_FILE) as f:
        card_id = 0
        for line in [line.strip() for line in f]:
            # drop everything before colon
            line = line.split(":")[1]

            # card numbers are 1-increment
            card_id += 1

            # parse the lists of numbers
            winning_number_list = [int(val) for val in line.split("|")[0].split()]
            card_number_list = [int(val) for val in line.split("|")[1].split()]

            # iterate through numbers on card to check for winners
            card_winners = 0
            for num in card_number_list:
                if num in winning_number_list:
                    card_winners += 1

            # instantiate card and add to lists
            new_card = Card(card_id, card_winners)
            card_dict[card_id] = new_card
            card_open_list.append(new_card)

    while len(card_open_list) > 0:
        test_card = card_open_list.pop()  # pop a card off open list
        card_closed_list.append(test_card)

        # check for any bonus cards, and add them to the open list
        bonus_cards = test_card.get_bonus_card_ids()
        for card_id in bonus_cards:
            card_open_list.append(card_dict[card_id])

    # score is the length of the closed list
    print(len(card_closed_list))
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
