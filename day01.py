""" Day 1 of Advent of Code 2023 """
import re

NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("day01.txt", "r", encoding="utf8") as f:
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
    for line in CALIBRATION_DOCUMENT.splitlines():
        pattern = re.compile(r"(one|two|three|four|five|six|seven|eight|nine)")
        m = re.search(pattern, line)
        while m is not None:
            line = (
                line[: m.start()]
                + m[0][0]
                + str(NUMBERS.index(m[0]) + 1)
                + m[0][-1]
                + line[m.end() :]
            )
            m = re.search(pattern, line)

        nums = re.sub(r"[a-z]", "", line)
        value += int(nums[0] + nums[-1])

    return value


print(part1())
print(part2())
