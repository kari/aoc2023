""" Day 4 of AoC 2023 """
import re
from typing import List

DEBUG = False

if DEBUG:
    INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    PART1 = 35
    PART2 = None
else:
    with open("inputs/day05.txt", "r", encoding="utf8") as f:
        INPUT = f.read()
    PART1 = 379811651
    PART2 = None

MAP_PATTERN = re.compile(r"([^-\n]+)-to-([^-]+) map:\n((?:.+(?:\n|$))+)")


class Map:
    def __init__(self, data):
        self.source: str = data[0]
        self.dest: str = data[1]
        self.ranges: List[List[int]] = list(
            map(lambda x: [int(y) for y in x.split()], data[2].splitlines())
        )

    def __str__(self):
        return f"{self.source}-to-{self.dest} map"

    def __repr__(self):
        return f"Map('{self.source}','{self.dest}',...)"

    def convert(self, number: int):
        for r in self.ranges:
            dest, source, length = r
            if number in range(source, source + length + 1):
                offset = number - source
                return dest + offset
        return number


seeds = map(int, re.match(r"seeds: (.+)", INPUT)[1].split())  # pyright: ignore[reportOptionalSubscript]
maps = list(map(Map, re.findall(MAP_PATTERN, INPUT)))

locations = []
for s in seeds:
    idx = s
    for m in maps:
        idx = m.convert(idx)
    locations.append(idx)

print(min(locations))
assert min(locations) == PART1
