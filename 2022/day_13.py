# Advent of code 2022
# Day 13

def get_data():
    with open("day_13_data.txt") as f:
        pairs = []
        while True:
            # Eval converts string representation of list to list
            list1 = eval(f.readline().strip())
            list2 = eval(f.readline().strip())
            pairs.append([list1, list2])

            linebreak = f.readline()
            if (linebreak != '\n'):
                break # Skip newline

    return pairs


def compare(left, right):
    # True
    if left < right:
        return 1
    # False
    elif left > right:
        return -1
    # Neutral
    else:
        return 0


def compare_lists(left, right):
    """Compare 2 lists to establish correct order"""

    if type(left) == int and type(right) == int:
        return compare(left, right)

    elif type(left) == int and type(right) == list:
        return compare_lists([left], right)

    elif type(left) == list and type(right) == int:
        return compare_lists(left, [right])

    elif type(left) == list and type(right) == list:
        for l, r in zip(left, right):
            outcome = compare_lists(l, r)
            # If not neutral (0), then return, otherwise, move to next pair
            if outcome != 0:
                return outcome

        return compare_lists(len(left), len(right))


def part1(data):
    sum = 0
    for i, pairs in enumerate(data, 1):
        in_order = compare_lists(*pairs)  # Extract the pairs into separate lists
        if in_order == 1:
            sum += i  # Increment the sum by the index of those pairs that are in the correct order

    print("Part1:", sum)


data = get_data()
part1(data)
