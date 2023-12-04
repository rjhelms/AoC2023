from time import perf_counter

IN_FILE = "04/input.txt"

if __name__ == "__main__":
    start_time = perf_counter()

    score = 0

    with open(IN_FILE) as f:
        card_number = 0
        for line in [line.strip() for line in f]:
            # drop everything before colon
            line = line.split(":")[1]

            # card numbers are 1-increment
            card_number += 1

            # parse the lists of numbers
            winning_number_list = [int(val) for val in line.split("|")[0].split()]
            card_number_list = [int(val) for val in line.split("|")[1].split()]

            # iterate through numbers on card to check for winners and score
            card_score = 0
            for num in card_number_list:
                if num in winning_number_list:
                    if card_score == 0:
                        card_score = 1
                    else:
                        card_score *= 2
            score += card_score

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
