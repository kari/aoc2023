""" Day 9 of AoC 2023 """
import numpy as np

DEBUG = False

if DEBUG:
    INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()
    PART1 = 114
    PART2 = 2
else:
    with open("inputs/day09.txt", "r", encoding="utf8") as f:
        INPUT = f.read().splitlines()
    PART1 = 2038472161
    PART2 = 1091

history = list(map(lambda x: list(map(int, x.split())), INPUT))
next_values = []
for h in history:
    last_digits = [h[-1]]
    diff = h.copy()
    while any([x != 0 for x in diff]):
        diff = np.diff(diff)
        last_digits.append(diff[-1])
    next_values.append(np.cumsum(list(reversed(last_digits)))[-1])

print(sum(next_values))
assert sum(next_values) == PART1

prev_values = []
for h in history:
    first_digits = [h[0]]
    diff = h.copy()
    while any([x != 0 for x in diff]):
        diff = np.diff(diff)
        first_digits.append(diff[0])
    first_digits = list(reversed(first_digits))
    xtr = [0]
    for i in range(1, len(first_digits)):
        xtr.append(first_digits[i] - xtr[i - 1])
    prev_values.append(xtr[-1])

print(sum(prev_values))
assert sum(prev_values) == PART2
