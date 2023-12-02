from time import perf_counter

IN_FILE = "02/input.txt"

if __name__ == "__main__":
    start_time = perf_counter()
    score = 0
    with open(IN_FILE) as f:
        for line in f:
            game, rounds = line.strip().split(": ")
            game = int(game.split(" ")[-1])
            rounds = rounds.split("; ")
            valid = True
            bag = {}
            for round in rounds:
                pulls = [x.split(" ") for x in round.split(", ")]
                for pull in pulls:
                    if (pull[1] not in bag) or (int(pull[0]) > bag[pull[1]]):
                        bag[pull[1]] = int(pull[0])
            power = 1
            for color in bag:
                power = power * bag[color]
            score += power

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
