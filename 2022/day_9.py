# Advent of code 2022
# Day 9
import math


def get_data():
    with open("day_9_data.txt") as f:
        instructions = [line.strip().split(' ') for line in f]
        
    return instructions


def part1(instructions):
    head_pos, tail_pos = [0,0], [0,0]   # Initialise starting positions of the head, tail
    tail_pos_history = [[0,0]]  # History of where the tail visited at least once

    for command in instructions:
        direction, num = command[0], int(command[1])
        
        for i in range(num):
            prev_head_pos = head_pos.copy()  # Initialise previous position of the head

            # Move head incrementally for num steps
            if direction == 'R':
                head_pos[0] += 1
            elif direction == 'L':
                head_pos[0] -= 1
            elif direction == 'U':
                head_pos[1] += 1
            elif direction == 'D':
                head_pos[1] -= 1
            
            # Calculate euclidean distance and check if the distance is 2 or more  
            if math.dist(head_pos, tail_pos) >= 2.0:
                # Check if head and tail are in the same axis
                if (head_pos[0] == tail_pos[0]) or (head_pos[1] == tail_pos[1]):
                    tail_pos = prev_head_pos  # Move tail to previous head position
                else:
                    # Move tail diagonally

                    # Get direction to move tail based on the where the head is from the tail
                    tail_pos[0] += int(math.copysign(1, (head_pos[0]-tail_pos[0])))
                    tail_pos[1] += int(math.copysign(1, (head_pos[1]-tail_pos[1])))
                
                # Store position of tail if it hasn't visited before
                if tail_pos not in tail_pos_history:
                    tail_pos_history.append(tail_pos.copy())

    print("Part 1:", len(tail_pos_history))


def part2(instructions):
    # Initialise starting positions of all parts of the rope
    rope_len = 10  
    rope_positions = [[0,0].copy() for i in range(rope_len)]

    tail_pos_history = [[0,0]]  # History of where the tail visited at least once

    for command in instructions:
        direction, num = command[0], int(command[1])
        
        for i in range(num):            
            # Move head incrementally for num steps
            if direction == 'R':
                rope_positions[0][0] += 1
            elif direction == 'L':
                rope_positions[0][0] -= 1
            elif direction == 'U':
                rope_positions[0][1] += 1
            elif direction == 'D':
                rope_positions[0][1] -= 1

            for rope_index in range(1, len(rope_positions)):
                # Calculate euclidean distance and check if the distance is 2 or more
                # between current rope part and the previous part
                
                if math.dist(rope_positions[rope_index], rope_positions[(rope_index-1)]) >= 2.0:
                    # If current part and previous part are in the x-axis
                    if (rope_positions[(rope_index-1)][0] == rope_positions[rope_index][0]):
                        # Move current part in the y-axis
                        rope_positions[rope_index][1] += int(math.copysign(1, (rope_positions[(rope_index-1)][1]-rope_positions[rope_index][1])))
                    
                    # If current part and previous part are in the y-axis
                    elif (rope_positions[(rope_index-1)][1] == rope_positions[rope_index][1]):
                        # Move current part in the x-axis
                        rope_positions[rope_index][0] += int(math.copysign(1, (rope_positions[(rope_index-1)][0]-rope_positions[rope_index][0])))
                    
                    else:
                        # Move current part diagonally

                        # Get direction to move current part based on the where the previous part is
                        rope_positions[rope_index][0] += int(math.copysign(1, (rope_positions[(rope_index-1)][0]-rope_positions[rope_index][0])))
                        rope_positions[rope_index][1] += int(math.copysign(1, (rope_positions[(rope_index-1)][1]-rope_positions[rope_index][1])))
                    
                # Store position of tail if it hasn't visited before
                tail_pos = rope_positions[(rope_len-1)].copy()
                if tail_pos not in tail_pos_history:
                    tail_pos_history.append(tail_pos)

    print("Part 2:", len(tail_pos_history))

instructions = get_data()
part1(instructions)
part2(instructions)
