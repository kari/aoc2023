""" Day 1 of Advent of Code 2023 """
import re

NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("inputs/day01.txt", "r", encoding="utf8") as f:
    CALIBRATION_DOCUMENT = f.read()


def part1():
    """Part 1"""
    value = 0
    for line in CALIBRATION_DOCUMENT.splitlines():
        nums = re.sub(r"[a-z]", "", line)
        value += int(nums[0] + nums[-1])

    return value


def part2():
    """Part 2"""
    value = 0
    pattern = re.compile(rf"({"|".join(NUMBERS)})")
    for line in CALIBRATION_DOCUMENT.splitlines():
        m = re.search(pattern, line)
        while m is not None:
            line = (
                line[: m.start()]
                + str(NUMBERS.index(m[0]) + 1)
                + line[m.end() - 1:]
            )
            m = re.search(pattern, line)

        nums = re.sub(r"[a-z]", "", line)
        value += int(nums[0] + nums[-1])

    return value

p1 = part1()
assert p1 == 54450
print(p1)

p2 = part2()
assert p2 == 54265
print(p2)
