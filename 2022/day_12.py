# Advent of code 2022
# Day 12

import numpy as np
import dijkstra 
import string

def alphabet_pos(char):
    if char == 'S':
        return 0  # Smallest value
    elif char == 'E':
        return 27  # Largest value
    else:
        return (string.ascii_lowercase.index(char)+1)


def get_data():
    grid = None
    
    with open("day_12_data.txt") as f:
        for line in f:
            characters = list(line.strip())

            if grid is None:
                grid = np.empty((0, len(characters)), dtype=int)
                        
            x = np.array([alphabet_pos(char) for char in characters]).reshape((1,-1))
            
            grid = np.vstack([grid, x])

    return grid


def create_graph(grid):
    """
    Creates a directed graph from the grid
    """
    graph = dijkstra.Graph()
    
    
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            current_node = f"{i},{j}"  # Node name is the index position in the grid
            current_node_val = grid[i,j]
            
            """
            Check in each direction if a node exists 
            """
            try:
                next_node_val = grid[i-1,j]  # Up
                next_node = f"{i-1},{j}"
                
                distance = (next_node_val - current_node_val)
                if distance <= 1:
                    graph.add_edge(current_node, next_node, 1)

            except IndexError:
                pass

            try:
                next_node_val = grid[i+1,j]  # Down
                next_node = f"{i+1},{j}"
                
                distance = (next_node_val - current_node_val)
                if distance <= 1:
                    graph.add_edge(current_node, next_node, 1)
            except IndexError:
                pass

            try:
                next_node_val = grid[i,j-1]  # Left
                next_node = f"{i},{j-1}"
                
                distance = (next_node_val - current_node_val)
                if distance <= 1:
                    graph.add_edge(current_node, next_node, 1)
            except IndexError:
                pass

            try:
                next_node_val = grid[i,j+1]  # Right
                next_node = f"{i},{j+1}"
                
                distance = (next_node_val - current_node_val)
                if distance <= 1:
                    graph.add_edge(current_node, next_node, 1)
            except IndexError:
                pass

    return graph


def part1(grid):
    # Get positon of start and end nodes (S and E)
    start_node_index = np.argwhere(grid == 0)[0]
    end_node_index = np.argwhere(grid == 27)[0]


    START_NODE = f"{start_node_index[0]},{start_node_index[1]}"
    END_NODE = f"{end_node_index[0]},{end_node_index[1]}"
    
    # Update end node to have 26 as its value (matches 'z')
    grid[end_node_index[0], end_node_index[1]] = 26
    
    # Apply dijkstra algorithm to graph
    graph = create_graph(grid)
    dijkstra_process = dijkstra.DijkstraSPF(graph, START_NODE)
    
    path = dijkstra_process.get_path(END_NODE)
   
    print("Part 1:", (len(path)-1))


def part2(grid):
    # Get positon of start and end nodes (S and E)
    start_node_index = np.argwhere(grid == 0)[0]
    end_node_index = np.argwhere(grid == 27)[0]  
    
    END_NODE = f"{end_node_index[0]},{end_node_index[1]}"

    # Update start node to have 1 as its value (matches 'a')
    grid[start_node_index[0], start_node_index[1]] = 1

    # Update end node to have 26 as its value (matches 'z')
    grid[end_node_index[0], end_node_index[1]] = 26

    path_lengths = []  # Store shortest path of each journey
    graph = create_graph(grid)
    
    # Loop through all positions where the node has value 1
    for pos in np.argwhere(grid == 1):
        start_node = f"{pos[0]},{pos[1]}"
        
        try:
            # Apply dijkstra algorithm to graph for different starting nodes
            dijkstra_process = dijkstra.DijkstraSPF(graph, start_node)
            path = dijkstra_process.get_path(END_NODE)
            path_lengths.append((len(path)-1))
        except:
            pass
   
    print("Part 2:", min(path_lengths))


grid = get_data()
part1(grid)

grid = get_data()
part2(grid)