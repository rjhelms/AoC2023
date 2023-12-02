from time import perf_counter

IN_FILE = "01/input.txt"

NUMBERS = []
if __name__ == "__main__":
    start_time = perf_counter()

    with open(IN_FILE) as f:
        for line in f:
            value = 0
            for char in line:
                if char.isdigit():
                    value = int(char) * 10
                    break
            for char in line[::-1]:
                if char.isdigit():
                    value += int(char)
                    break
            NUMBERS.append(value)

    result = 0
    for value in NUMBERS:
        result += value

    print(result)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
