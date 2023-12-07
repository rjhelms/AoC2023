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

    time = 0
    race = 0

    with open(IN_FILE) as f:
        time = int("".join(f.readline().split(":")[1].split()))
        distance = int("".join(f.readline().split(":")[1].split()))

    b = time
    c = -distance

    high = (-b - sqrt((b**2) - (4 * -1 * c))) / -2
    low = (-b + sqrt((b**2) - (4 * -1 * c))) / -2

    if low == ceil(low):
        low = int(low + 1)
    else:
        low = ceil(low)
    high = ceil(high)
    score = high - low

    print(score)
    end_time = perf_counter()
    print(f"Execution time: {end_time-start_time:.3f}s")
