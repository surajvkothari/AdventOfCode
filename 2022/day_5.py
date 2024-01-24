# Advent of code 2022
# Day 5

import numpy as np
from collections import deque

def get_data():
    with open("day_5_data.txt") as f:
        crate_grid = []
        instructions = []

        num_cols = 0
        load_stack_data = True

        for line in f:
            # Check if crate stack data has been loaded
            if len(line) == 1:
                # Stop loading create stack data
                load_stack_data = False
                continue  # Skip to loading instructions data

            if load_stack_data:
                # Extract the crate letters from each row
                line_split = list(line.strip('\n'))[1::4]

                if line_split[0] == '1':
                    num_cols = len(line_split)
                    continue # Skip line of column indexes
                else:
                    # Store crates letters
                    grid_row = np.array(line_split)
                    if len(grid_row) < num_cols:
                        # Add empty crates to fill all columns
                        grid_row = np.pad(np.array(line_split), (0, num_cols-len(grid_row)), mode="constant", constant_values=" ")

                    crate_grid.append(grid_row)
            else:
                # Load instructions data
                instructions.append(line.strip())

        crate_grid = np.array(crate_grid)
        crate_stacks = []

        for col in crate_grid.T:
            stack = deque(col[col != ' '])
            crate_stacks.append(stack)

    return crate_stacks, instructions


def part1(crate_stacks, instructions):
    for i in instructions:
        instruction_separated = i.split()

        num_crates_moved = int(instruction_separated[1])
        from_col = int(instruction_separated[3])
        to_col = int(instruction_separated[5])

        for n in range(num_crates_moved):
            # Move each crate from one stack onto the other
            crate = crate_stacks[from_col-1].popleft()
            crate_stacks[to_col-1].appendleft(crate)

    print("Part 1:")
    # Show which crates are on the top
    for stack in crate_stacks:
        print(stack.popleft(), end="")


def part2(crate_stacks, instructions):
    for i in instructions:
        instruction_separated = i.split()

        num_crates_moved = int(instruction_separated[1])
        from_col = int(instruction_separated[3])
        to_col = int(instruction_separated[5])

        crates_moved = []
        for n in range(num_crates_moved):
            crate = crate_stacks[from_col-1].popleft()
            # Move each crate into a queue
            crates_moved.append(crate)

        # Append all the moved crates in reverse order
        crate_stacks[to_col-1].extendleft(crates_moved[::-1])

    print("\nPart 2:")
    # Show which crates are on the top
    for stack in crate_stacks:
        print(stack.popleft(), end="")


crate_stacks, instructions = get_data()
part1(crate_stacks, instructions)

crate_stacks, instructions = get_data()
part2(crate_stacks, instructions)
