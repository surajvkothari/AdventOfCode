# Advent of code 2017
# Day 1

def get_data():
    with open("day_1_data.txt") as f:
        return f.read().strip()


def part1(seq):
    seq = [int(x) for x in seq]
    digit_matches = []

    for i in range(len(seq)):
        # List is circular, so wrap around to the beginning when i is at the end
        if seq[i] == seq[ (i+1) % len(seq) ]:
            digit_matches.append(seq[i])

    print("Part 1:", sum(digit_matches))


def part2(seq):
    seq = [int(x) for x in seq]
    digit_matches = []

    for i in range(len(seq)):
        # List is circular, so wrap around to the beginning when i is at the end
        # Compare to the digit halfway around the circular list
        if seq[i] == seq[ (i+len(seq)//2) % len(seq) ]:
            digit_matches.append(seq[i])

    print("Part 2:", sum(digit_matches))


seq = get_data()
part1(seq)
part2(seq)

