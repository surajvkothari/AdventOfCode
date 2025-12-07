# Advent of Code: 2015
# Day 2

def get_data():
    with open("day_2_data.txt") as f:
        dimensions = []

        for line in f:
            # Split each measurement of dimension and convert into int
            dimension = [int(i) for i in line.strip().split('x')]
            dimensions.append(dimension)
    
    return dimensions


def wrapping_formula(l, w, h):
    # Slack is the area of the smallest side
    slack = min([l*w, w*h, l*h])

    return 2*l*w + 2*w*h + 2*h*l + slack

def ribbon_formula(l, w, h):
    # Ribbon is the smallest face's perimeter
    ribbon = min([2*l+2*w, 2*w+2*h, 2*l+2*h])
    bow = l*w*h  # Cubic volume

    return ribbon + bow


def part1(data):
    total = 0
    
    for dimension in data:
        # Unpack dimension when passing to formula
        total += wrapping_formula(*dimension)

    print("PART 1:", total)


def part2(data):
    total = 0
    
    for dimension in data:
        # Unpack dimension when passing to formula
        total += ribbon_formula(*dimension)

    print("PART 2:", total)


data = get_data()
part1(data)
part2(data)