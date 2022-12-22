# Advent of code 2021
# Day 5

import numpy as np

def get_data():
    with open("day_5_data.txt") as f:
        lines = []
        for line in f:
            # Remove new line and split by arrow
            endpoints = line.strip().split(" -> ")
            # Separate start and end coords
            start = tuple(map(int, endpoints[0].split(',')))
            end = tuple(map(int, endpoints[1].split(',')))

            lines.append([start, end])

    return lines

def get_new_grid(lines):
    # Return nxn grid of 0s
    lines = np.array(lines)
    max = np.max(lines)
    return np.zeros((max+1,max+1))


def part1(lines, grid):
    for line in lines:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]

        # x-coords are equal
        if x1 == x2:
            # Make sure starting point is the smaller one
            iter = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)
            # Iterate vertically along y-coords
            for i in iter:
                grid[i][x1] += 1  # Increment value at the point

        # y-coords are equal
        elif y1 == y2:
            # Make sure starting point is the smaller one
            iter = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
            # Iterate horizontally along x-coords
            for i in iter:
                grid[y1][i] += 1  # Increment value at the point

    # Return the number of points greater than or equal to 2
    print("Part 1:", np.sum(grid >= 2))


def part2(lines, grid):
    for line in lines:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]

        # x-coords are equal
        if x1 == x2:
            # Make sure starting point is the smaller one
            iter = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)
            # Iterate vertically along y-coords
            for i in iter:
                grid[i][x1] += 1  # Increment value at the point

        # y-coords are equal
        elif y1 == y2:
            # Make sure starting point is the smaller one
            iter = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
            # Iterate horizontally along x-coords
            for i in iter:
                grid[y1][i] += 1  # Increment value at the point
        # Diagonal
        else:
            # Start from the first pair of coords
            x, y = x1, y1

            # Make sure starting point is the smaller one
            iter = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)

            # Iteratate the n steps between points
            for n in iter:
                grid[y][x] += 1
                # Increment if start is smaller, else decrement
                if x1 < x2:
                    x += 1
                else:
                    x -= 1

                # Increment if start is smaller, else decrement
                if y1 < y2:
                    y += 1
                else:
                    y -= 1

    # Return the number of points greater than or equal to 2
    print("Part 2:", np.sum(grid >= 2))


lines = get_data()
grid = get_new_grid(lines)
part1(lines, grid)

grid = get_new_grid(lines)
part2(lines, grid)
