# Advent of code 2022
# Day 3

def get_data():
    with open("day_3_data.txt") as f:
        strings = [line.strip() for line in f]

    return strings

def get_priority(char):
    if char.isupper():
        # Maps uppercase chars to range [27-52]
        return ord(char) - 38
    else:
        # Maps lowercase chars to range [1-26]
        return ord(char) - 96

def get_duplicate_char(string):
    """ Gets duplicate char in both halves of the string """
    first_half = string[:len(string)//2]
    second_half = string[len(string)//2:]

    for char in first_half:
        if char in second_half:
            return char


def part1(strings):
    total_priority = 0
    for string in strings:
        char = get_duplicate_char(string)
        total_priority += get_priority(char)

    print("Part 1:", total_priority)


def part2(strings):
    pass


strings = get_data()
part1(strings)
