""" Day 3 of AoC 2023 """
import re

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
    PART2 = None
else:
    with open("day03.txt", "r", encoding="utf8") as f:
        SCHEMATIC = f.read().splitlines()
    PART1 = None
    PART2 = None

NUMBER = re.compile(r"(\d+)")
SYMBOL = re.compile(r"[^0-9\.]")
part_sum = 0
for idx, line in enumerate(SCHEMATIC):
    lines = (max(idx-1,0), min(idx+1, len(SCHEMATIC)-1))
    for m in NUMBER.finditer(line):
        span = (max(m.start()-1,0), min(m.end(), len(line)-1))
        for l in range(lines[0], lines[1]+1):
            for c in range(span[0], span[1]+1):
                if SYMBOL.match(SCHEMATIC[l][c]):
                    part_sum += int(m[0])

print(part_sum)
