from time import perf_counter

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

    current_step = "AAA"
    step_count = 0
    move_idx = 0

    while current_step != "ZZZ":
        move = steps[move_idx]
        if move == "L":
            current_step = map[current_step][0]
        else:
            current_step = map[current_step][1]
        step_count += 1
        move_idx = step_count % len(steps)

    print(step_count)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
