""" Day 9 of AoC 2023 """
import numpy as np

DEBUG = True

if DEBUG:
    INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()
    PART1 = 114
    PART2 = None
else:
    with open("inputs/day09.txt", "r", encoding="utf8") as f:
        INPUT = f.read().splitlines()
    PART1 = None
    PART2 = None

history = list(map(lambda x: list(map(int, x.split())), INPUT))
next_values = []
for h in history:
    last_digits = [h[-1]]
    diff = h.copy()
    while sum(diff) != 0:
        diff = np.diff(diff)
        last_digits.append(diff[-1])
    print(list(reversed(last_digits)))
    print(np.cumsum(list(reversed(last_digits))))
    next_values.append(np.cumsum(list(reversed(last_digits)))[-1])
print(sum(next_values))