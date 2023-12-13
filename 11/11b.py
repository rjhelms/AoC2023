from time import perf_counter

IN_FILE = "11/input.txt"

EXPAND_DISTANCE = 1000000


# rather than expanding lists, add the extra space in distance calculations
def manhattan_distance(start, end, empty_rows, empty_columns):
    distance = abs(start[0] - end[0])
    for i in range(min(start[0], end[0]), max(start[0], end[0])):
        if i in empty_columns:
            distance += EXPAND_DISTANCE - 1

    distance += abs(start[1] - end[1])

    for i in range(min(start[1], end[1]), max(start[1], end[1])):
        if i in empty_rows:
            distance += EXPAND_DISTANCE - 1
    return distance


def visualize(universe):
    for row in universe:
        row_string = ""
        for point in row:
            if point == 1:
                row_string += "#"
            else:
                row_string += "."
        print(row_string)


if __name__ == "__main__":
    start_time = perf_counter()
    universe = []

    with open(IN_FILE) as f:
        for row in f:
            line = []
            for char in row.strip():
                if char == "#":
                    line.append(1)
                else:
                    line.append(0)
            universe.append(line)

    # identify the empty rows and columns
    empty_rows = []
    empty_columns = []
    for i in range(len(universe)):
        if sum(universe[i]) == 0:
            empty_rows.append(i)
    for i in range(len(universe[0])):
        if sum([x[i] for x in universe]) == 0:
            empty_columns.append(i)

    # find position of all galaxies
    positions = []
    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if universe[y][x] == 1:
                positions.append((x, y))

    score = 0
    while len(positions) > 0:
        this_galaxy = positions.pop()
        for that_galaxy in positions:
            score += manhattan_distance(
                this_galaxy, that_galaxy, empty_rows, empty_columns
            )

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
