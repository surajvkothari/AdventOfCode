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

instructions = get_data()
part1(instructions)
