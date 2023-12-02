from time import perf_counter

IN_FILE = "02/input.txt"

BAG = {"red": 12, "green": 13, "blue": 14}

if __name__ == "__main__":
    start_time = perf_counter()
    score = 0
    with open(IN_FILE) as f:
        for line in f:
            game, rounds = line.strip().split(": ")
            game = int(game.split(" ")[-1])
            rounds = rounds.split("; ")
            valid = True
            for round in rounds:
                pulls = [x.split(" ") for x in round.split(", ")]
                for pull in pulls:
                    if int(pull[0]) > BAG[pull[1]]:
                        valid = False
                        break
            if valid:
                score += game

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
