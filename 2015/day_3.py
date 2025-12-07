# Advent of Code: 2015
# Day 3

def get_data():
    with open("day_3_data.txt") as f:
        moves = list(f.readline())
    
    return moves


def part1(data):
    location = [0, 0]  # Starting location
    houses_visited = {(0,0): 1}  # Stores location and count of visits

    for move in data:
        # NORTH
        if move == '^':
            location = (location[0], location[1] + 1)
        # SOUTH
        elif move == 'v':
            location = (location[0], location[1] - 1)
        # EAST
        elif move == '>':
            location = (location[0] + 1, location[1])
        # WEST
        elif move == '<':
            location = (location[0] - 1, location[1])
        
        # Check for a repeated visit
        if location in houses_visited.keys():
            houses_visited[location] += 1  # Increment visited count
        else:
            # Add a new location
            houses_visited[location] = 1

    print("PART 1:", len(houses_visited))


def part2(data):
    santa_location, robo_location = [0, 0], [0, 0]  # Starting locations

    houses_visited = {(0,0): 1}  # Stores location and count of visits

    for index, move in enumerate(data):
        # SANTA's MOVE
        if index % 2 == 0:
            # NORTH
            if move == '^':
                santa_location = (santa_location[0], santa_location[1] + 1)
            # SOUTH
            elif move == 'v':
                santa_location = (santa_location[0], santa_location[1] - 1)
            # EAST
            elif move == '>':
                santa_location = (santa_location[0] + 1, santa_location[1])
            # WEST
            elif move == '<':
                santa_location = (santa_location[0] - 1, santa_location[1])
            
            # Check for a repeated visit
            if santa_location in houses_visited.keys():
                houses_visited[santa_location] += 1  # Increment visited count
            else:
                # Add a new location
                houses_visited[santa_location] = 1

        # ROBOT SANTA's MOVE
        else:
            # NORTH
            if move == '^':
                robo_location = (robo_location[0], robo_location[1] + 1)
            # SOUTH
            elif move == 'v':
                robo_location = (robo_location[0], robo_location[1] - 1)
            # EAST
            elif move == '>':
                robo_location = (robo_location[0] + 1, robo_location[1])
            # WEST
            elif move == '<':
                robo_location = (robo_location[0] - 1, robo_location[1])
            
            # Check for a repeated visit
            if robo_location in houses_visited.keys():
                houses_visited[robo_location] += 1  # Increment visited count
            else:
                # Add a new location
                houses_visited[robo_location] = 1

    print("PART 2:", len(houses_visited))

data = get_data()
part1(data)
part2(data)