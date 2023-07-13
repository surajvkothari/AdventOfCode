# Advent of code 2022
# Day 6

def get_data():
    with open("day_6_data.txt") as f:
        string = f.readline().strip()

    return string


def part1(data):
    for i, char in enumerate(data):
        index = i + 1
        if index > 4:
            buffer = data[(i-4):i]  # Get a moving window of 4 chars

            # Check buffer has only unique chars
            if len(set(buffer)) == len(buffer):
                break

    print("Part 1:", index-1)  # Subtract 1 from index


def part2(data):
    for i, char in enumerate(data):
        index = i + 1
        if index > 14:
            buffer = data[(i-14):i]  # Get a moving window of 4 chars

            # Check buffer has only unique chars
            if len(set(buffer)) == len(buffer):
                break

    print("Part 2:", index-1)  # Subtract 1 from index


data = get_data()
part1(data)
part2(data)
