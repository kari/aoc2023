""" Day 8 of AoC 2023 """
from __future__ import annotations
import re
import math
from itertools import cycle

DEBUG = False

if DEBUG:
    INPUT = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()
    INPUT2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()
    PART1 = 6
    PART2 = 6
else:
    with open("inputs/day08.txt", "r", encoding="utf8") as f:
        INPUT = f.read().splitlines()
    PART1 = 14257
    PART2 = 16187743689077

INSTRUCTIONS = list(INPUT[0])


class Node:
    def __init__(self, name: str, left: Node | None = None, right: Node | None = None):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node('{self.name}','{self.left.name if self.left is not None else "None"}','{self.right.name if self.right is not None else "None"}')"


NODE_PATTERN = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")


def build_network(rows=INPUT):
    network: dict[str, Node] = {}
    for row in rows[2:]:
        m = NODE_PATTERN.match(row)
        assert m
        node, left, right = m.groups()
        # print(node, left, right)
        if left not in network:
            network[left] = Node(left)
        if right not in network:
            network[right] = Node(right)
        if node not in network:
            network[node] = Node(node, network[left], network[right])
        else:
            node = network[node]
            node.left = network[left]
            node.right = network[right]

    # print(NETWORK)
    return network


def part1(network):
    node = network["AAA"]
    assert node
    steps = 0
    for i in cycle(INSTRUCTIONS):  # FIXME: can be infinite loop
        steps += 1
        if i == "L":
            node = node.left
        else:
            node = node.right
        assert node
        if node.name == "ZZZ":
            # print(steps)
            break

    return steps


def part2(network, instructions):
    nodes = list(
        map(lambda x: network[x], filter(lambda x: x[-1] == "A", network.keys()))
    )
    periods: list[int] = []
    for node in nodes:
        steps = 0
        for i in cycle(instructions):  # FIXME: can be infinite loop
            steps += 1
            if i == "L":
                node = node.left
            else:
                node = node.right
            assert node
            if node.name[-1] == "Z":
                periods.append(steps)
                break

    return math.lcm(*periods)


def main():
    network = build_network()
    steps = part1(network)
    print(steps)
    assert steps == PART1

    instructions = list(INPUT[0])
    if DEBUG:
        assert INPUT2
        instructions = INPUT2[0]
        network = build_network(INPUT2)

    steps = part2(network, instructions)
    print(steps)
    assert steps == PART2


main()
