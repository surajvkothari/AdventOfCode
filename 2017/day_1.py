# Advent of code 2017
# Day 1

def get_data():
    with open("day_1_data.txt") as f:
        return f.read().strip()


def part1(seq):
    seq = [int(x) for x in seq]
    digit_matches = []

    for i in range(len(seq)):
        if i == (len(seq)-1):
            # List is circular, so wrap around to the beginning when i is at the end
            if seq[i] == seq[0]:
                digit_matches.append(seq[i])
        else:
            # Check if the next digit matches
            if seq[i] == seq[i+1]:
                digit_matches.append(seq[i])

    print("Part 1:", sum(digit_matches))

seq = get_data()
part1(seq)

