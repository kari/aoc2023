""" Day 4 of AoC 2023 """
import re
import math

DEBUG = False

if DEBUG:
    CARDS = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    PART1 = 13
    PART2 = 30
else:
    with open("inputs/day04.txt", "r", encoding="utf8") as f:
        CARDS = f.read()
    PART1 = 25231
    PART2 = 9721255


def matches(c):
    left, right = c.split(" | ")
    left = set(map(int, re.sub(r"Card\s+\d+:\s+", "", left).split()))
    right = set(map(int, right.split()))
    return len(left.intersection(right))


points = 0
for card in CARDS.splitlines():
    points += math.floor(2 ** (matches(card) - 1))

print(points)
assert points == PART1


def incr(idx, val=1):
    # global cards
    if idx in cards:
        cards[idx] += val
    else:
        cards[idx] = val


cards = {}

for num, card in enumerate(CARDS.splitlines()):
    incr(num)
    for i in range(matches(card)):
        incr(num + i + 1, cards[num])

print(sum(cards.values()))
assert sum(cards.values()) == PART2
