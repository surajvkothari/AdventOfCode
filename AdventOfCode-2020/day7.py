# Advent of code 2020
# Day 7

""" Part 1 """

def get_key_value(line):
    line = line[:-1] # Remove space

    contains = line.split(" contain ")

    key = contains[0][:-5]
    values = contains[1].split(", ")

    # Remove numbers
    values = [v[2:] for v in values]

    # Removes " bags" or " bag"
    values = [v[:-5] if " bags" in v else v[:-4] for v in values]

    return (key, values)


def create_bags_dict():
    bags = {}

    with open("day7_data.txt") as f:
        for line in f:
            line = line.strip("\n")
            k, v = get_key_value(line)
            bags[k] = v

    return bags

def get_outer_bags(bag_node):
    outer = []
    for key in bags:
        if bag_node in bags[key]:
            outer.append(key)

    return outer

bags = create_bags_dict()

outer_bags = []
bags_queue = []
shiny_gold_outer = get_outer_bags("shiny gold")
bags_queue.extend(shiny_gold_outer)
outer_bags.extend(shiny_gold_outer)

while len(bags_queue) > 0:
    key = bags_queue.pop() # Remove a key from the queue
    outer_bags_key = get_outer_bags(key)
    outer_bags.extend(outer_bags_key)
    bags_queue.extend(outer_bags_key)

print("Part1:",len(set(outer_bags)))

""" Part 2 """


def get_key_value2(line):
    line = line[:-1] # Remove space

    contains = line.split(" contain ")

    key = contains[0][:-5]
    values = contains[1].split(", ")

    # Removes " bags" or " bag"
    values = [v[:-5] if " bags" in v else v[:-4] for v in values]

    return (key, values)

def create_bags_dict2():
    bags = {}

    with open("day7_data.txt") as f:
        for line in f:
            line = line.strip("\n")
            k, v = get_key_value2(line)
            bags[k] = v

    return bags


def get_num_bags(bag):
    sum = 0

    bag_children = bags2[bag]
    #print(bag, bag_children)
    for b in bag_children:
        if b == "no other":
            continue
        else:
            num = int(b[:2])
            child_bag = b[2:]

            sum += num
            sum += num * get_num_bags(child_bag)

    return sum

bags2 = create_bags_dict2()
print("Part2:",get_num_bags("shiny gold"))
