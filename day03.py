""" Day 3 of AoC 2023 """
import re
import math

DEBUG = False

if DEBUG:
    SCHEMATIC = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()
    PART1 = 4361
    PART2 = 467835
else:
    with open("inputs/day03.txt", "r", encoding="utf8") as f:
        SCHEMATIC = f.read().splitlines()
    PART1 = 550064
    PART2 = 85010461

SYMBOL = re.compile(r"[^0-9\.]")

gears = {}
part_sum = 0

for idx, line in enumerate(SCHEMATIC):
    lines = (max(idx-1,0), min(idx+1, len(SCHEMATIC)-1))
    for m in re.finditer(r"(\d+)", line):
        span = (max(m.start()-1,0), min(m.end(), len(line)-1))
        for l in range(lines[0], lines[1]+1):
            for c in range(span[0], span[1]+1):
                if SYMBOL.match(SCHEMATIC[l][c]):
                    part_sum += int(m[0])
                if SCHEMATIC[l][c] == "*":
                    if (l,c) in gears:
                        gears[(l,c)].append(int(m[0]))
                    else:
                        gears[(l,c)] = [int(m[0])]

print(part_sum)
assert part_sum == PART1

gear_ratio_sum = sum(math.prod(value) for (key, value) in gears.items() if len(value) == 2)
print(gear_ratio_sum)
assert gear_ratio_sum == PART2
