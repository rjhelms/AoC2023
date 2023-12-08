from time import perf_counter
from math import lcm

IN_FILE = "08/input.txt"

if __name__ == "__main__":
    start_time = perf_counter()

    map = {}
    steps = ""

    with open(IN_FILE) as f:
        lines = f.readlines()
        steps = lines[0].strip()
        for row in lines[2:]:
            map[row[0:3]] = (row[7:10], row[12:15])

    # build list of all starting nodes
    start_nodes = []
    for key in map.keys():
        if key[-1] == "A":
            start_nodes.append(key)

    # traverse from each, to build list of path lengths
    path_lengths = []
    for node in start_nodes:
        current_step = node
        step_count = 0
        move_idx = 0

        while current_step[-1] != "Z":
            move = steps[move_idx]
            if move == "L":
                current_step = map[current_step][0]
            else:
                current_step = map[current_step][1]
            step_count += 1
            move_idx = step_count % len(steps)
        path_lengths.append(step_count)

    # answer is least common multiple of lengths
    print(lcm(*path_lengths))

    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
