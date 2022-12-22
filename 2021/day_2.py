# Advent of code 2021
# Day 2

def get_data():
    with open("day_2_data.txt") as f:
        instructions = [line.split() for line in f]

    return instructions

def part1(instructions):
    horizonatal = 0
    depth = 0

    for ins in instructions:
        cmd = ins[0]
        amount = int(ins[1])

        if cmd == "forward":
            horizonatal += amount
        elif cmd == "up":
            depth -= amount
        elif cmd == "down":
            depth += amount

    print("Part1:", horizonatal*depth)


def part2(instructions):
    horizonatal = 0
    depth = 0
    aim = 0

    for ins in instructions:
        cmd = ins[0]
        amount = int(ins[1])

        if cmd == "forward":
            horizonatal += amount
            depth += (aim * amount)
        elif cmd == "up":
            aim -= amount
        elif cmd == "down":
            aim += amount

    print("Part2:", horizonatal*depth)

instructions = get_data()
part1(instructions)
part2(instructions)
