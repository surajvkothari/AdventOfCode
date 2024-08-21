# Advent of code 2022
# Day 14

import numpy as np

"""
Cave symbols:
0: Air
1: Rocks
2: Sand
"""

def get_data():    
    with open("day_14_data.txt") as f:
        paths = []
        for line in f:
            path = line.strip().split(" -> ")
            # For each pair of coords, convert to integers and store as a tuple 
            path = [tuple([int(i) for i in coords.split(',')]) for coords in path]
            paths.append(path)           

    return paths


def get_cave_size(paths):
    """ Returns the size of the cave as number of rows/cols """
    x_coords, y_coords = [coords[0] for path in paths for coords in path], [coords[1] for path in paths for coords in path]

    num_rows = max(y_coords) + 2  # +2 for including the 0th row and a row for the abyss
    num_cols = (max(x_coords) - min(x_coords)) + 3  # +3 for including a 0th column and for including a column on either end

    x_coord_shift = min(x_coords) - 1 # Shift the x coordinates to start from 0
    
    return (num_rows, num_cols), x_coord_shift


def store_rocks(cave, paths, x_shift):
    for path in paths: 
        # Get all coordinates except the last
        for coord_index in range(0,len(path)-1):
            start_coord, end_coord = path[coord_index], path[coord_index+1]
                        
            start_x_coord = start_coord[0] - x_shift  # Shifts the x coordinates to start from 0
            start_y_coord = start_coord[1]

            end_x_coord = end_coord[0] - x_shift  # Shifts the x coordinates to start from 0
            end_y_coord = end_coord[1]

            if start_x_coord == end_x_coord:
                # Vertical Line
                if start_y_coord < end_y_coord:
                    line_range = range(start_y_coord, end_y_coord+1)
                else:
                    line_range = range(end_y_coord, start_y_coord+1)

                for i in line_range:
                    cave[i, start_x_coord] = 1  # Add rock

            elif start_y_coord == end_y_coord:
                # Horizontal Line
                if start_x_coord < end_x_coord:
                    line_range = range(start_x_coord, end_x_coord+1)
                else:
                    line_range = range(end_x_coord, start_x_coord+1)

                for i in line_range:
                    cave[start_y_coord, i] = 1  # Add rock


def simulate_sand(cave, x_shift):
    """ Simulates the falling of sand """
    sand_counter = 0
    not_in_abyss = True
    
    while not_in_abyss:
        sand_position = (0, 500-x_shift)  # Initial position of sand

        not_stopped = True

        while not_stopped:
            # Check for space below
            new_sand_position = (sand_position[0]+1, sand_position[1])
            
            if cave[new_sand_position] == 0:
                sand_position = new_sand_position
            else:
                # Check for space diagonally left
                new_sand_position = (sand_position[0]+1, sand_position[1]-1)
                
                if cave[new_sand_position] == 0:
                    sand_position = new_sand_position
                else:
                    # Check for space diagonally right
                    new_sand_position = (sand_position[0]+1, sand_position[1]+1)

                    if cave[new_sand_position] == 0:
                        sand_position = new_sand_position
                    # Sand has stopped moving
                    else:
                        cave[sand_position] = 2  # Add sand
                        sand_counter += 1

                        # Sand has been blocked from the top
                        if sand_position == (0, 500-x_shift):
                            not_in_abyss = False
                        
                        not_stopped = False                

            # If sand has entered the abyss
            if sand_position[0] == (cave.shape[0]-1):
                not_stopped = False
                not_in_abyss = False
    
    return sand_counter
    

def part1(paths):
    cave_shape, x_shift = get_cave_size(paths)
    cave = np.zeros(cave_shape)
    store_rocks(cave, paths, x_shift)

    sand_counter = simulate_sand(cave, x_shift)
    print("Part 1:", sand_counter)
  

def part2(paths):
    cave_shape, x_shift = get_cave_size(paths)
    
    # Add floor at the bottom of the cave whose length is double the cave's size
    paths.append([(x_shift//2, cave_shape[0]), (x_shift*2, cave_shape[0])])

    cave_shape, x_shift = get_cave_size(paths)
    
    cave = np.zeros(cave_shape)
    store_rocks(cave, paths, x_shift)

    # Drop air spaces surrounding the floor (all rows up to floor and 1st, 2nd last cols)
    cave = cave[:-1, 1:-1]
    
    sand_counter = simulate_sand(cave, x_shift)
    
    print("Part 2:", sand_counter)
    

paths = get_data()
part1(paths)
part2(paths)