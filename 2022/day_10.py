# Advent of code 2022
# Day 10

import numpy as np

def get_data():
    with open("day_10_data.txt") as f:
        instructions = [line.strip() for line in f]

    return instructions


def part1(instructions):
    register_X = 1
    cycle = 0

    signal_strengths = []

    for op in instructions:
        cycle += 1
        # Store the cycle number multiplied by value at register_X
        signal_strengths.append(cycle*register_X)

        if op == "noop":
            # Do nothing
            pass
        else:
            # Increment cycle as part of addx instruction
            cycle += 1
            # Store the cycle number multiplied by value at register_X
            signal_strengths.append(cycle*register_X)

            # Addx instruction
            value = int(op.split()[1])
            register_X += value

    signals = np.array([20,60,100,140,180,220]) - 1  # -1 to index from 0
    sum_signals = np.array(signal_strengths)[signals].sum()

    print("Part 1:", sum_signals)


def part2(instructions):
    CRT_grid = np.zeros(240)

    sprite_position = 1
    cycle = 0

    for op in instructions:
        cycle += 1

        # Check if CRT pointer is in the same position as the 3-pixel sprite
        CRT_pointer = cycle-1
        if (CRT_pointer % 40) in [sprite_position-1,sprite_position,sprite_position+1]:
            CRT_grid[CRT_pointer] = 1

        if op == "noop":
            # Do nothing
            pass
        else:
            # Increment cycle as part of addx instruction
            cycle += 1

            # Check if CRT pointer is in the same position as the 3-pixel sprite
            CRT_pointer = cycle-1
            if (CRT_pointer % 40) in [sprite_position-1,sprite_position,sprite_position+1]:
                CRT_grid[CRT_pointer] = 1

            # Addx instruction
            value = int(op.split()[1])
            sprite_position += value

    np.set_printoptions(linewidth=np.inf)  # Disable output wrapping
    print("Part 2:")
    print(CRT_grid.reshape(6, 40))  # Reshape into 6 rows by 40 cols

instructions = get_data()

part1(instructions)
part2(instructions)
