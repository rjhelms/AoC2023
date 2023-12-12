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


def visualize(tile_map):
    for row in tile_map:
        row_string = ""
        for val in row:
            match val:
                case -2:
                    row_string += "░"
                case -1:
                    row_string += " "
                case 0:
                    row_string += "●"
                case 3:
                    row_string += "└"
                case 5:
                    row_string += "│"
                case 6:
                    row_string += "┌"
                case 9:
                    row_string += "┘"
                case 10:
                    row_string += "─"
                case 12:
                    row_string += "┐"
        print(row_string)


def is_in_bounds(position, tile_map):
    # validate position is in bounds
    if position[0] < 0 or position[1] < 0:
        return False
    if position[1] >= len(tile_map):
        return False
    if position[0] >= len(tile_map[0]):
        return False
    return True


def is_valid(position, open_list, closed_list, tile_map):
    if not is_in_bounds(position, tile_map):
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

        # to do part B calculations, need to get actual shape of start position
        is_start = position == start_positon
        if is_start:
            tile_map[position[1]][position[0]] = 0

        # check each direction that this pipe joins to for reciprocal connection
        if value & NORTH:
            check_position = (position[0], position[1] - 1)
            if is_valid(check_position, open_list, closed_list, tile_map):
                if tile_map[check_position[1]][check_position[0]] & SOUTH:
                    if is_start:
                        tile_map[position[1]][position[0]] += NORTH
                    open_list.append(check_position)
        if value & EAST:
            check_position = (position[0] + 1, position[1])
            if is_valid(check_position, open_list, closed_list, tile_map):
                if tile_map[check_position[1]][check_position[0]] & WEST:
                    if is_start:
                        tile_map[position[1]][position[0]] += EAST
                    open_list.append(check_position)
        if value & SOUTH:
            check_position = (position[0], position[1] + 1)
            if is_valid(check_position, open_list, closed_list, tile_map):
                if tile_map[check_position[1]][check_position[0]] & NORTH:
                    if is_start:
                        tile_map[position[1]][position[0]] += SOUTH
                    open_list.append(check_position)
        if value & WEST:
            check_position = (position[0] - 1, position[1])
            if is_valid(check_position, open_list, closed_list, tile_map):
                if tile_map[check_position[1]][check_position[0]] & EAST:
                    if is_start:
                        tile_map[position[1]][position[0]] += WEST
                    open_list.append(check_position)

    # cull tile_map - anything not in closed list gets set to 0
    for y in range(len(tile_map)):
        for x in range(len(tile_map[0])):
            if (x, y) not in closed_list:
                tile_map[y][x] = 0

    # generate dual map - each tile expended to 2x2
    dual_map = []
    for row in tile_map:
        dual_row_1 = []
        dual_row_2 = []
        for val in row:
            dual_row_1.append(val)
            if (val & (EAST + SOUTH)) == EAST + SOUTH:
                dual_row_1.append(EAST + WEST)
                dual_row_2.append(NORTH + SOUTH)
            elif val & EAST:
                dual_row_1.append(EAST + WEST)
                dual_row_2.append(0)
            elif val & SOUTH:
                dual_row_1.append(0)
                dual_row_2.append(NORTH + SOUTH)
            else:
                dual_row_1.append(0)
                dual_row_2.append(0)
            dual_row_2.append(0)
        dual_map.append(dual_row_1)
        dual_map.append(dual_row_2)

    # flood fill dual map
    y = 0
    for row in dual_map:
        x = 0
        for tile in row:
            if tile == 0:
                in_bounds = True
                open_list = [(x, y)]
                closed_list = []
                while len(open_list) > 0:
                    position = open_list.pop()
                    closed_list.append(position)
                    # check each direction
                    for check_position in [
                        (position[0], position[1] - 1),
                        (position[0], position[1] + 1),
                        (position[0] - 1, position[1]),
                        (position[0] + 1, position[1]),
                    ]:
                        if not is_in_bounds(check_position, dual_map):
                            in_bounds = False
                        elif (
                            is_valid(check_position, open_list, closed_list, dual_map)
                            and dual_map[check_position[1]][check_position[0]] == 0
                        ):
                            open_list.append(check_position)
                for item in closed_list:
                    if in_bounds:
                        dual_map[item[1]][item[0]] = -2  # interior empty cell
                    else:
                        dual_map[item[1]][item[0]] = -1  # exterior empty cell
            x += 1
        y += 1

    interior_count = 0

    # check each cell in the original map to see if it was found as interior in the dual map
    for y in range(len(tile_map)):
        for x in range(len(tile_map[0])):
            if dual_map[y * 2][x * 2] == -2:
                interior_count += 1
            tile_map[y][x] = dual_map[y * 2][x * 2]

    # visualize(tile_map)

    print(interior_count)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
