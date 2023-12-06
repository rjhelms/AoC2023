from time import perf_counter

IN_FILE = "05/input.txt"


class Map:
    def __init__(self, in_type: str, out_type: str) -> None:
        self.in_type = in_type
        self.out_type = out_type
        self.map_rows: list[MapRow] = []

    def get_mapping(self, in_value: int) -> int:
        for row in self.map_rows:
            check_value = row.get_mapping(in_value)
            if check_value:
                return check_value

        return in_value

    def __repr__(self) -> str:
        return f"{self.in_type}-to-{self.out_type}: {len(self.map_rows)} mappings"


class MapRow:
    def __init__(self, in_line: list[int]) -> None:
        self.base_out = in_line[0]
        self.base_in = in_line[1]
        self.map_range = in_line[2]

    def get_mapping(self, in_value: int) -> int:
        offset = in_value - self.base_in
        if offset >= 0 and offset < self.map_range:
            return self.base_out + offset
        return None


if __name__ == "__main__":
    start_time = perf_counter()

    seeds: list[int] = []
    maps: list[Map] = []
    lines: list[str] = []

    with open(IN_FILE) as f:
        lines = [line.strip() for line in f.readlines()]

    seeds = [int(val) for val in lines.pop(0).split(":")[1].split()]
    lines.pop(0)  # pop the blank line

    # parse mappings
    new_map: bool = True  # is the next line the start of a new map?
    this_map: Map = None

    while len(lines) > 0:
        line = lines.pop(0)
        if new_map:
            line = line.split()[0].split("-")
            this_map = Map(line[0], line[-1])
            new_map = False
        elif len(line) == 0:
            # blank line means we're done
            maps.append(this_map)
            new_map = True
        else:
            line = [int(val) for val in line.split()]
            this_map.map_rows.append(MapRow(line))

    maps.append(this_map)  # append the last one

    score = float("inf")

    for value in seeds:
        for map in maps:
            value = map.get_mapping(value)
        if value < score:
            score = value

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
