# Advent of code 2022
# Day 4

def get_data():
    with open("day_4_data.txt") as f:
        strings = [line.strip().split(',') for line in f]

    return strings


def check_fully_contains(range1, range2):
    range1_in_range2 = all(i in range2 for i in range1)
    range2_in_range1 = all(i in range1 for i in range2)

    return (range1_in_range2 or range2_in_range1)


def check_part_contains(range1, range2):
    range1_in_range2 = any(i in range2 for i in range1)
    range2_in_range1 = any(i in range1 for i in range2)

    return (range1_in_range2 or range2_in_range1)


def part1(data):
    count = 0
    for pair in data:
        # Gets the start and end values of the range as integers
        pair1_endpoints, pair2_endpoints = [int(i) for i in pair[0].split('-')],\
                                            [int(i) for i in pair[1].split('-')]

        # Increment endpoint by 1 otherwise range will not include it
        pair1_endpoints[1] += 1
        pair2_endpoints[1] += 1

        # Converts list of endpoints to python range object
        range1, range2 = range(*pair1_endpoints), range(*pair2_endpoints)

        if check_fully_contains(range1, range2):
            count += 1

    print("Part 1:", count)


def part2(data):
    count = 0
    for pair in data:
        # Gets the start and end values of the range as integers
        pair1_endpoints, pair2_endpoints = [int(i) for i in pair[0].split('-')],\
                                            [int(i) for i in pair[1].split('-')]

        # Increment endpoint by 1 otherwise range will not include it
        pair1_endpoints[1] += 1
        pair2_endpoints[1] += 1

        # Converts list of endpoints to python range object
        range1, range2 = range(*pair1_endpoints), range(*pair2_endpoints)

        if check_part_contains(range1, range2):
            count += 1

    print("Part 2:", count)


data = get_data()
part1(data)
part2(data)
