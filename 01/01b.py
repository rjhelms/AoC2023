from time import perf_counter

IN_FILE = "01/input.txt"

STRINGS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
NUMBERS = []

def find_digit_at_index(string, index):
    substring = string[index:]
    # check from part A - is it a digit?
    if substring[:1].isdigit():
        return int(substring[:1])

    # else, start checking for text values
    for i in range(len(STRINGS)):
        check_length = len(STRINGS[i])
        if len(string[index:]) < check_length:
            continue
        if string[index:index+check_length] == STRINGS[i]: 
            return i+1
    return None

if __name__ == "__main__":
    start_time = perf_counter()

    with open(IN_FILE) as f:
        for line in f:
            line = line.strip()
            value = 0
            for i in range(len(line)):
                result = find_digit_at_index(line, i)
                if result:
                    value = result * 10
                    break
            for i in range(len(line), -1, -1):
                result = find_digit_at_index(line, i)
                if result:
                    value += result
                    break
            print(line, value)
            NUMBERS.append(value)

    result = 0
    for value in NUMBERS:
        result += value
    
    print(result)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
