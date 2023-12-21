# Advent of code 2023
# Day 14
import numpy as np

def get_data():
    with open("day_14_data.txt") as f:
        # Convert data into 2D numpy grid
        platform = np.array([np.array(list(row.strip())) for row in f])

    return platform


def roll_north(platform):
    tilted_platform = platform.copy()

    for i in range(tilted_platform.shape[0]):
        for j in range(tilted_platform.shape[1]):
            if tilted_platform[i,j] == 'O':
                # Get buffer of previous elements in the current column
                prev_elements = tilted_platform[:i,j]

                # Remove spaces from the end ('.')
                for item in np.flip(prev_elements):
                    if item == '.':
                        prev_elements = prev_elements[:-1]
                    else:
                        break

                # Length of previous elements (after spaces removed) is the position of the rock after tilting
                new_tilt_position = prev_elements.shape[0]

                # Check new position is different
                if (new_tilt_position,j) != (i,j):
                    # Move rock into new position on tilted platform
                    tilted_platform[new_tilt_position,j] = 'O'
                    tilted_platform[i,j] = '.'

    return tilted_platform


def roll_west(platform):
    tilted_platform = platform.copy()

    for i in range(tilted_platform.shape[0]):
        for j in range(tilted_platform.shape[1]):
            if tilted_platform[i,j] == 'O':
                # Get buffer of previous elements in the current row
                prev_elements = tilted_platform[i,:j]

                # Remove spaces from the end ('.')
                for item in np.flip(prev_elements):
                    if item == '.':
                        prev_elements = prev_elements[:-1]
                    else:
                        break

                # Length of previous elements (after spaces removed) is the position of the rock after tilting
                new_tilt_position = prev_elements.shape[0]

                # Check new position is different
                if (i,new_tilt_position) != (i,j):
                    # Move rock into new position on tilted platform
                    tilted_platform[i,new_tilt_position] = 'O'
                    tilted_platform[i,j] = '.'

    return tilted_platform


def calculate_load(platform):
    row_load = platform.shape[0]  # Initialise load of each row to the length of the platform
    total_load = 0

    for row in platform:
        # Count number of round rocks and multiply by row load
        total_load += np.count_nonzero(row == 'O') * row_load
        row_load -= 1

    return total_load


def spin_cycle(platform):
    tilted_platform = roll_north(platform)
    tilted_platform = roll_west(tilted_platform)
    # Tilt south
    tilted_platform = np.flip(roll_north(np.flip(tilted_platform, axis=0)), axis=0)
    # Tilit east
    tilted_platform = np.flip(roll_west(np.flip(tilted_platform, axis=1)), axis=1)

    return tilted_platform


def part1(platform):
    tilted_platform = roll_north(platform)
    total_load = calculate_load(tilted_platform)
    print("Part 1:", total_load)


def part2(platform):
    """
    Find duplicate cycle
    """
    tilted_platform = platform
    tilted_platform_strings = []
    duplicate_cycle_nums = []

    cycle_num = 0
    while True:
        tilted_platform = spin_cycle(tilted_platform)
        cycle_num += 1

        # Convert platform grid into 1D string
        tilted_platform_str = "".join(tilted_platform.flatten())
        if tilted_platform_str in tilted_platform_strings:
            duplicate_cycle_num = tilted_platform_strings.index(tilted_platform_str) + 1

            # Store duplicate cycles
            if duplicate_cycle_num in duplicate_cycle_nums:
                break  # Exit out of while loop

            duplicate_cycle_nums.append(duplicate_cycle_num)
    
        tilted_platform_strings.append("".join(tilted_platform.flatten()))

    # Get the start/end of the duplicate cycles
    duplicate_cycle_start, duplicate_cycle_end = duplicate_cycle_nums[0], duplicate_cycle_nums[-1]

    """
    Find reduced number of spins and calculate load on the final tilted platform
    """
    total_spins = 1_000_000_000
    reduced_spins = (total_spins - duplicate_cycle_start) % (duplicate_cycle_end - duplicate_cycle_start + 1) + duplicate_cycle_start

    final_tilted_platform = platform
    for i in range(reduced_spins):
        final_tilted_platform = spin_cycle(final_tilted_platform)

    total_load = calculate_load(final_tilted_platform)
    print("Part 2:", total_load)


platform = get_data()
part1(platform)
part2(platform)
