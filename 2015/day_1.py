# Advent of code 2015
# Day 1

def get_data():
    with open("day_1_data.txt") as f:
        brackets = list(f.readline())
    
    return brackets


def part1(data):
    floor = 0
    for char in data:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    print("PART 1:", floor)


data = get_data()
part1(data)