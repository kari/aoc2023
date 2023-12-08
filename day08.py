""" Day 8 of AoC 2023 """
from __future__ import annotations
import re
from itertools import cycle

DEBUG = False

if DEBUG:
    INPUT = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()
    PART1 = 6
    PART2 = None
else:
    with open("inputs/day08.txt", "r", encoding="utf8") as f:
        INPUT = f.read().splitlines()
    PART1 = 14257
    PART2 = None

INSTRUCTIONS = list(INPUT[0])


class Node:
    def __init__(self, name: str, left: Node | None = None, right: Node | None = None):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node('{self.name}','{self.left.name}','{self.right.name}')"


NODE_PATTERN = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
NETWORK: dict[str, Node] = {}

def build_network():
    for row in INPUT[2:]:
        node, left, right = NODE_PATTERN.match(row).groups()
        # print(node, left, right)
        if left not in NETWORK:
            NETWORK[left] = Node(left)
        if right not in NETWORK:
            NETWORK[right] = Node(right)
        if node not in NETWORK:
            NETWORK[node] = Node(node, NETWORK[left], NETWORK[right])
        else:
            node = NETWORK[node]
            node.left = NETWORK[left]
            node.right = NETWORK[right]

    # print(NETWORK)

def part1():
    node = NETWORK["AAA"]
    steps = 0
    for i in cycle(INSTRUCTIONS): # FIXME: can be infinite loop
        steps += 1
        if i == "L":
            node = node.left
        else:
            node = node.right
        if node.name == "ZZZ":
            # print(steps)
            break

    return steps


build_network()
steps = part1()
print(steps)
assert steps == PART1
