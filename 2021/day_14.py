# Advent of code 2021
# Day 14

import time

def part1():
    """ Part 1 """
    global template
    global pair_insertions
    global polymer_string

    element_counts = {}
    for element in template:
        if element not in element_counts:
            element_counts[element] = 1
        else:
            element_counts[element] += 1

    for iteration in range(10):
        insertions_num = 0
        # Iterate up to last element
        for index in range(len(template)-1):
            pair_left = template[index]
            pair_right = template[index+1]

            # Combine left and right to form a pair
            pair = pair_left + pair_right
            insertion_element = pair_insertions[pair]

            # Insert after current index (+1) and after the number of insertions
            # up to the current stage (insertions_num)
            polymer_string.insert(index+insertions_num+1, insertion_element)

            insertions_num += 1

            # Set new element count to 1 or increment if it already exists
            if insertion_element not in element_counts:
                element_counts[insertion_element] = 1
            else:
                element_counts[insertion_element] += 1

        template = "".join(polymer_string)  # Turn template into string

    # Calculate the maximum count - minimum count of elements
    element_counts_vals = element_counts.values()
    print("Difference:", max(element_counts_vals) - min(element_counts_vals))


def update_element_counts(element, count):
    """ Updates the count of the element """
    global element_counts

    if element not in element_counts:
        element_counts[element] = count
    else:
        element_counts[element] += count


def update_pair_counts(pair, count):
    """ Updates the count of the pair """
    global new_pair_counts

    if pair not in new_pair_counts:
        new_pair_counts[pair] = count
    else:
        new_pair_counts[pair] += count


def calculate_element_counts(pair_counts):
    """ Calculates the number of elements from the total count of pairs """
    global template

    for pair, count in pair_counts.items():
        # Always get the first element from pair as second is overlapped, so
        # the second one will be counted in the next iteration
        element = pair[0]
        update_element_counts(element, count)

    # The last element in the template is not included in the loop,
    # so update it now
    last_element = template[-1]
    update_element_counts(last_element, 1)


def part2():
    """ Part 2 """
    global template
    global pair_insertions
    global new_pair_counts
    global element_counts
    global step_limit

    pair_counts = {}
    # Initialise pair counts by getting the pairs from the template
    for index in range(len(template)-1):
        pair_left = template[index]
        pair_right = template[index+1]

        # Combine left and right to form a pair
        pair = pair_left + pair_right

        if pair not in pair_counts:
            pair_counts[pair] = 1
        else:
            pair_counts[pair] += 1

    for step in range(step_limit):
        new_pair_counts = {}  # New pair counts for new step

        for pair, count in pair_counts.items():
            insertion_element = pair_insertions[pair]
            # Form the new pairs using the insertion element
            new_pair1 = pair[0] + insertion_element
            new_pair2 = insertion_element + pair[1]

            update_pair_counts(new_pair1, count)
            update_pair_counts(new_pair2, count)

        pair_counts = new_pair_counts

    calculate_element_counts(pair_counts)

    # Calculate the maximum count - minimum count of elements
    element_counts_vals = element_counts.values()
    print("Difference:", max(element_counts_vals) - min(element_counts_vals))


def get_data():
    pair_insertions = {}
    with open("day_14_data.txt") as f:
        for line in f:
            line_split = line.split(" ")
            pair = line_split[0]
            insertion = line_split[2].rstrip()
            pair_insertions[pair] = insertion

    return pair_insertions


template = "CBNBOKHVBONCPPBBCKVH"
pair_insertions = get_data()
polymer_string = list(template)

start = time.time()
part1()
end = time.time()
print("P1 time:", end-)

print()

template = "CBNBOKHVBONCPPBBCKVH"  # Reset for part 2
pair_insertions = get_data()
element_counts = {}
step_limit = 40

start = time.time()
part2()
end = time.time()
print("P2 time:", end-start)
