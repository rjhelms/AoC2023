from time import perf_counter
from math import ceil, sqrt

IN_FILE = "06/input.txt"

# x = hold time
# a = time of race
# y = distance travelled

# distance = (time-hold)*hold
# distance = time*hold-hold^2
# 0 = -hold^2 + time*hold - distance

# a = -1
# b = time
# c = -distance

if __name__ == "__main__":
    start_time = perf_counter()

    races = []

    with open(IN_FILE) as f:
        times = [int(x) for x in f.readline().split(":")[1].split()]
        distances = [int(x) for x in f.readline().split(":")[1].split()]
        races = zip(times, distances)

    score = 1

    for race in races:
        b = race[0]
        c = -race[1]

        high = (-b - sqrt((b**2) - (4 * -1 * c))) / -2
        low = (-b + sqrt((b**2) - (4 * -1 * c))) / -2

        if low == ceil(low):
            low = int(low + 1)
        else:
            low = ceil(low)
        high = ceil(high)
        score *= high - low

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
