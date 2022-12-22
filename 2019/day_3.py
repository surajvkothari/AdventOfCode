# Advent of code 2019
# Day 3

"""
Optimised version taken from:
https://dev.to/jbristow/advent-of-code-2019-solution-megathread-day-3-crossed-wires-3f4b
"""

data = []
with open("data.txt") as f:
    for line in f:
        lineSplit = line.strip("\n").split(",")

        data.append(lineSplit)

""" Part 1 """

def getCoords(data):
    x = 0
    y = 0
    step = 0
    coords = {}

    for move in data:
        direction = move[0]
        distance = int(move[1:])

        # Pick in which direction to move
        move_x = move_y = 0
        if direction == "L":
            move_x = -1
        if direction == "R":
            move_x = 1
        if direction == "D":
            move_y = -1
        if direction == "U":
            move_y = 1

        # Do the actual movement
        for _ in range(0, distance):
            x += move_x
            y += move_y

            step += 1

            if (x,y) not in coords:
                coords[(x,y)] = step

    return coords


def getNearestDistance(coords):
    distances = [abs(c[0]) + abs(c[1]) for c in coords]

    return min(distances)

wire1 = getCoords(data[0])
wire2 = getCoords(data[1])

intersections = set(list(wire1.keys())) & set(list(wire2.keys()))

nearestDistance = getNearestDistance(intersections)
print(nearestDistance)

""" Part 2 """
def get_fewest():
    combined_steps = [wire1[i] + wire2[i] for i in intersections]
    return min(combined_steps)

print(get_fewest())
