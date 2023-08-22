# Advent of code 2022
# Day 8

import numpy as np

def get_data():
    with open("day_8_data.txt") as f:
        grid = [list(row.strip()) for row in f]

        # Char to integer
        grid = [[int(i) for i in row] for row in grid]

        # Add -1 to start and end of each row
        for row in grid:
            row.insert(0, -1)
            row.append(-1)

        # Add row of -1 to start and end of grid
        num_cols = len(grid[0])
        border_row = [-1] * num_cols

        grid.insert(0, border_row)
        grid.append(border_row)

    return np.array(grid)


def part1(grid):
    num_rows, num_cols = grid.shape

    visible_count = 0

    for i in range(1, num_rows-1):
        for j in range(1, num_cols-1):
            current_tree = grid[i,j]
            tree_row = grid[i]
            tree_col = grid[:,j]

            # Check in every direction if the trees are smaller
            check_left = np.all(tree_row[:j] < current_tree)
            check_right = np.all(tree_row[j+1:] < current_tree)
            check_top = np.all(tree_col[:i] < current_tree)
            check_bottom = np.all(tree_col[i+1:] < current_tree)

            # If any direction is visible, increase count
            if np.any([check_left, check_right, check_top, check_bottom]):
                visible_count += 1

    print("Part1:", visible_count)


def get_viewing_distance(view, tree):
    dist = 0
    for i in view:
        if i == -1:
            break
        else:
            dist += 1
            if i >= tree:
                break

    return dist


def part2(grid):
    num_rows, num_cols = grid.shape

    highest_scenic_score = 0

    for i in range(1, num_rows-1):
        for j in range(1, num_cols-1):
            current_tree = grid[i,j]
            tree_row = grid[i]
            tree_col = grid[:,j]

            # For every direction, get the viewing distance
            # Flip the left and top directions to count from left to right
            distance_left = get_viewing_distance(np.flip(tree_row[:j]), current_tree)
            distance_right = get_viewing_distance(tree_row[j+1:], current_tree)
            distance_top = get_viewing_distance(np.flip(tree_col[:i]), current_tree)
            distance_bottom = get_viewing_distance(tree_col[i+1:], current_tree)

            scenic_score = distance_left * distance_right * distance_top * distance_bottom

            highest_scenic_score = max(highest_scenic_score, scenic_score)

    print("Part2:", highest_scenic_score)

grid = get_data()
part1(grid)
part2(grid)
