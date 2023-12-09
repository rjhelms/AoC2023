from time import perf_counter
from collections import Counter

IN_FILE = "09/input.txt"

if __name__ == "__main__":
    start_time = perf_counter()

    score = 0

    with open(IN_FILE) as f:
        for row in f:
            # list of lists for each order of differences
            history = [[int(x) for x in row.split()]]

            # loop until the last iteration is all 0s
            while Counter(history[-1])[0] != len(history[-1]):
                # new list to store differences in last iteration
                new_history_line = []
                for i in range(1, len(history[-1])):
                    new_history_line.append(history[-1][i] - history[-1][i - 1])
                history.append(new_history_line)

            # iterate through difference lists backwards to extrapolate
            for i in range(len(history) - 2, -1, -1):
                # for part B, working back from start of list - so subtract, and insert at start of list
                history[i].insert(0, history[i][0] - history[i + 1][0])

            # for part B, score is initial value of first order
            score += history[0][0]

    print(score)

    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
