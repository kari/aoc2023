""" Day 7 of AoC 2023 """
from collections import Counter

DEBUG = True

if DEBUG:
    INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
    PART1 = 6440
    PART2 = 5905
else:
    with open("inputs/day07.txt", "r", encoding="utf8") as f:
        INPUT = f.read().splitlines()
    PART1 = 253603890
    PART2 = None

class Hand:
    ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, hand: str, bid: int):
        self.hand = list(hand)
        self.bid = bid

    def strength(self):
        counts = sorted(Counter(self.hand).values(), reverse=True)
        if counts[0] == 5: # five of a kind
            return 1
        elif counts[0] == 4: # four of a kind
            return 2
        elif counts[0] == 3 and counts[1] == 2: # full house
            return 3
        elif counts[0] == 3: # three of a kind
            return 4
        elif counts[0] == 2 and counts[1] == 2: # two pair
            return 5
        elif counts[0] == 2: # one pair
            return 6
        else: # high card
            return 7
        
    def __str__(self):
        return "".join(self.hand)

    def __repr__(self):
        return f'Hand(\'{"".join(self.hand)}\', {self.bid})'
    
    def sortorder(self):
        cmp = "".join(list(map(lambda x: chr(Hand.ORDER.index(x)), self.hand)))
        return str(self.strength())+cmp

hands = []
for row in INPUT:
    hand, bid = row.split()
    hand = Hand(hand, int(bid))
    hands.append(hand)


ranking = sorted(hands, key = lambda hand: hand.sortorder(), reverse=True)
winnings = 0
for rank, hand in enumerate(ranking):
    winnings += hand.bid * (rank+1)
print(winnings)
