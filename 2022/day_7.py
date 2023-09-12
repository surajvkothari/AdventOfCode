# Advent of code 2022
# Day 7

from treelib import Node, Tree

def get_data():
    with open("day_7_data.txt") as f:
        commands = [line.strip() for line in f]

    return commands


def create_filesystem_tree(commands):
    """ Creates a tree of the filesystem using the commands """
    filesystem = Tree()
    current_dir = '/_/'
    filesystem.create_node("dir", '/_/', data=0)

    ls_command = False
    total_dir_size = 0

    for line in commands:
        if line[0] == '$':
            # Line is a command
            command = line.split()
            instruction = command[1]
            if instruction == "cd":
                #print(current_dir, total_dir_size)
                filesystem[current_dir].data += total_dir_size
                if command[2] == "..":
                    parent_dir = filesystem.parent(current_dir).identifier
                    # Update parent directory size by adding current directory's size
                    filesystem[parent_dir].data += filesystem[current_dir].data
                    total_dir_size = 0 # Reset total directory size

                    current_dir = parent_dir  # Update current directory
                elif command[2] != "/":
                    # Store the total directory size for the current dir node
                    total_dir_size = 0 # Reset total directory size

                    current_dir_id = f"{command[2]}_{current_dir}"
                    current_dir = current_dir_id # Update current directory
        else:
            # Line is a file or directory
            output = line.split()
            if output[0] == "dir":
                # Create a directory node
                dir_name = output[1]
                dir_id = f"{dir_name}_{current_dir}"
                filesystem.create_node("dir", dir_id, parent=current_dir, data=0)


            else:
                # Create a file node
                filesize = int(output[0])
                filename = output[1]
                file_id = f"{filename}_{current_dir}"

                filesystem.create_node("file", file_id, parent=current_dir, data=filesize)

                # Increment directory filesize
                total_dir_size += filesize

    # Keep going back up the tree until root
    while filesystem.parent(current_dir):
        filesystem[current_dir].data += total_dir_size

        parent_dir = filesystem.parent(current_dir).identifier
        current_dir = parent_dir

    filesystem[current_dir].data += total_dir_size  # Store the total directory size for the root

    return filesystem


def part1(filesystem):
    total_size = 0

    for node_id in filesystem.expand_tree(mode=Tree.DEPTH):
        node = filesystem[node_id]
        if node.tag == "dir":
            if node.data < 100_000:
                total_size += node.data

    print("Part 1:", total_size)


def part2(filesystem):
    total_size = 0

    root_dir_size = filesystem["/_/"].data  # Get the size of the root directory

    unused_space = 70_000_000 - root_dir_size
    update_space = 30_000_000 - unused_space

    delete_dir_sizes = []  # Stores potential directories to be deleted

    for node_id in filesystem.expand_tree(mode=Tree.DEPTH):
        node = filesystem[node_id]
        if node.tag == "dir":
            if node.data >= update_space:
                delete_dir_sizes.append(node.data)

    # Get the smallest directory size
    delete_dir_total_size = min(delete_dir_sizes)
    print("Part 2:", delete_dir_total_size)


commands = get_data()
filesystem = create_filesystem_tree(commands)

part1(filesystem)
part2(filesystem)
