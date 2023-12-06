""" Day 2 of AoC 2023 """
import re
import math

DEBUG = False

if DEBUG:
    GAME_RECORD = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    PART1 = 8
    PART2 = 2286
else:
    with open("inputs/day02.txt", "r", encoding="utf8") as f:
        GAME_RECORD = f.read()
    PART1 = 2505
    PART2 = 70265


MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

GAME_PATTERN = re.compile(r"Game (\d+): (.+)")
CUBE_PATTERN = re.compile(r"(\d+) (\w+)")

id_sum = 0
cube_sum = 0
for line in GAME_RECORD.splitlines():
    max_seen = {"red": 0, "green": 0, "blue": 0}
    possible = True
    m = GAME_PATTERN.match(line)
    assert m is not None
    game_id, rounds = m[1], m[2]
    for r in rounds.split("; "):
        for c in r.split(", "):
            m = CUBE_PATTERN.match(c)
            assert m is not None
            if int(m[1]) > MAX_CUBES[m[2]]:
                possible = False
            if int(m[1]) > max_seen[m[2]]:
                max_seen[m[2]] = int(m[1])

    if possible:
        id_sum += int(game_id)

    cube_sum += math.prod(max_seen.values())

print(id_sum)
assert id_sum == PART1
print(cube_sum)
assert cube_sum == PART2
