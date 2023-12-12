from time import perf_counter

IN_FILE = "10/input.txt"

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

TILE_VALUES = {
    ".": 0,
    "|": NORTH + SOUTH,
    "-": EAST + WEST,
    "L": NORTH + EAST,
    "J": NORTH + WEST,
    "7": SOUTH + WEST,
    "F": SOUTH + EAST,
    "S": NORTH + EAST + SOUTH + WEST,  # start could connect from any direction
}


def is_valid(position, open_list, closed_list, tile_map):
    # validate position is in bounds
    if position[0] < 0 or position[1] < 0:
        return False
    if position[1] >= len(tile_map):
        return False
    if position[0] >= len(tile_map[0]):
        return False

    # validate position is not already in list
    if position in open_list:
        return False
    if position in closed_list:
        return False

    return True


if __name__ == "__main__":
    start_time = perf_counter()

    tile_map = []  # list of lists containing map of TILE_VALUES
    open_list = []
    closed_list = []
    start_positon = None

    with open(IN_FILE) as f:
        y = 0
        for row in f:
            row_list = []
            x = 0
            for char in row.strip():
                row_list.append(TILE_VALUES[char])
                if char == "S":
                    start_positon = (x, y)
                x += 1
            y += 1
            tile_map.append(row_list)

    open_list.append(start_positon)

    while len(open_list) > 0:
        position = open_list.pop()
        closed_list.append(position)

        value = tile_map[position[1]][position[0]]

        # check each direction that this pipe joins to for reciprocal connection
        if value & NORTH:
            check_position = (position[0], position[1] - 1)
            if is_valid(check_position, open_list, closed_list, tile_map):
                if tile_map[check_position[1]][check_position[0]] & SOUTH:
                    open_list.append(check_position)
        if value & EAST:
            check_position = (position[0] + 1, position[1])
            if is_valid(check_position, open_list, closed_list, tile_map):
                if tile_map[check_position[1]][check_position[0]] & WEST:
                    open_list.append(check_position)
        if value & SOUTH:
            check_position = (position[0], position[1] + 1)
            if is_valid(check_position, open_list, closed_list, tile_map):
                if tile_map[check_position[1]][check_position[0]] & NORTH:
                    open_list.append(check_position)
        if value & WEST:
            check_position = (position[0] - 1, position[1])
            if is_valid(check_position, open_list, closed_list, tile_map):
                if tile_map[check_position[1]][check_position[0]] & EAST:
                    open_list.append(check_position)

    print(len(closed_list) / 2)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
