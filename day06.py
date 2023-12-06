""" Day 6 of AoC 2023 """
import math

DEBUG = False

if DEBUG:
    INPUT = """Time:      7  15   30
Distance:  9  40  200""".splitlines()
    PART1 = 288
    PART2 = 71503
else:
    with open("inputs/day06.txt", "r", encoding="utf8") as f:
        INPUT = f.read().splitlines()
    PART1 = 2374848
    PART2 = 39132886

TIMES = list(map(int, INPUT[0].replace("Time:", "").split()))
DISTANCES = list(map(int, INPUT[1].replace("Distance:", "").split()))

ways = []
for (t, d) in zip(TIMES, DISTANCES):
    w = 0
    for a in range(0, t+1):
        if (t-a)*a > d:
            w += 1
    ways.append(w)

print(math.prod(ways))
assert math.prod(ways) == PART1

# the distance function is a downward opening parabola

TIME = int(INPUT[0].replace("Time:", "").replace(" ",""))
DISTANCE = int(INPUT[1].replace("Distance:", "").replace(" ",""))

win = 0
for i in range(0, math.floor(TIME/2)):
    if (TIME-i)*i > DISTANCE:
        win = i
        break
print(TIME-2*win+1)
assert (TIME-2*win+1) == PART2
