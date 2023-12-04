from time import perf_counter

IN_FILE = "03/input.txt"


class Number:
    def __init__(self, value: int, location: tuple, parts_list: list) -> None:
        self.value = value
        self.location = location
        self.parts_list = parts_list
        pass

    def append(self, value: int) -> None:
        self.value *= 10
        self.value += value

    def check_part(self) -> tuple:
        # in part 2, returns the location of the part, not just whether it exists
        length = len(str(self.value))

        # this is jank
        # check left and right
        if (self.location[0] - 1, self.location[1]) in self.parts_list:
            return (self.location[0] - 1, self.location[1])
        if (self.location[0] + length, self.location[1]) in self.parts_list:
            return (self.location[0] + length, self.location[1])

        # check above and below:
        for i in range(length):
            if (self.location[0] + i, self.location[1] - 1) in self.parts_list:
                return (self.location[0] + i, self.location[1] - 1)
            if (self.location[0] + i, self.location[1] + 1) in self.parts_list:
                return (self.location[0] + i, self.location[1] + 1)

        # check diagonals
        if (self.location[0] - 1, self.location[1] - 1) in self.parts_list:
            return (self.location[0] - 1, self.location[1] - 1)
        if (self.location[0] - 1, self.location[1] + 1) in self.parts_list:
            return (self.location[0] - 1, self.location[1] + 1)
        if (self.location[0] + length, self.location[1] - 1) in self.parts_list:
            return (self.location[0] + length, self.location[1] - 1)
        if (self.location[0] + length, self.location[1] + 1) in self.parts_list:
            return (self.location[0] + length, self.location[1] + 1)

        # no neighbour found
        return None

    def __repr__(self) -> str:
        return f"{self.location}: {self.value}"


if __name__ == "__main__":
    start_time = perf_counter()

    number_list = []
    parts_list = []

    with open(IN_FILE) as f:
        y_pos = 0
        lines = f.readlines()
        for line in lines:
            open_number = None
            x_pos = 0
            for char in line.strip():
                if char.isdigit():
                    if open_number:
                        open_number.append(int(char))
                    else:
                        open_number = Number(int(char), (x_pos, y_pos), parts_list)
                else:
                    if open_number:
                        number_list.append(open_number)
                        open_number = None
                    if char == "*":
                        parts_list.append((x_pos, y_pos))
                x_pos += 1

            # close any open numbers at end of line
            if open_number:
                number_list.append(open_number)

            y_pos += 1

    gear_ratios = {}
    gear_neighbours = {}

    for num in number_list:
        gear = num.check_part()
        if gear:
            if gear in gear_ratios:
                gear_ratios[gear] *= num.value
                gear_neighbours[gear] += 1
            else:
                gear_ratios[gear] = num.value
                gear_neighbours[gear] = 1

    score = 0
    for gear in gear_ratios:
        if gear_neighbours[gear] > 1:
            score += gear_ratios[gear]

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
