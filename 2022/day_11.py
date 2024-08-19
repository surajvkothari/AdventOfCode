# Advent of code 2022
# Day 11

class Monkey():
    def __init__(self, items, operator, op_value, div_check_val, 
                 true_throw_monkey, false_throw_monkey):
        
        self.items = items
        self.item_count = 0
        self.operator = operator
        self.op_value = op_value
        self.div_check_val = div_check_val
        self.true_throw_monkey = true_throw_monkey
        self.false_throw_monkey = false_throw_monkey
    
    def get_items(self):
        return self.items
    
    def get_item_count(self):
        return self.item_count
    
    def remove_item(self, item):
        self.items.remove(item)

    def get_throw_monkeys(self):
        return self.true_throw_monkey, self.false_throw_monkey
    
    def throw_item(self, item):
        """ Adds new item when an item is thrown """
        self.items.append(item)
    
    def operation(self, old):
        new = 0
        
        if self.operator == '+':
            if self.op_value == "old":
                new = old + old
            else:
                new = old + int(self.op_value)
        elif self.operator == '*':
            if self.op_value == "old":
                new = old * old
            else:
                new = old * int(self.op_value)
        
        new = int(new / 3)

        self.item_count += 1

        return new

    def check_divisibility(self, new):
        return new % self.div_check_val == 0


class Monkey2():
    def __init__(self, items, operator, op_value, div_check_val, 
                 true_throw_monkey, false_throw_monkey):
        
        self.items = items
        self.item_count = 0
        self.operator = operator
        self.op_value = op_value
        self.div_check_val = div_check_val
        self.true_throw_monkey = true_throw_monkey
        self.false_throw_monkey = false_throw_monkey
    
    def get_items(self):
        return self.items
    
    def get_item_count(self):
        return self.item_count
    
    def remove_item(self, item):
        self.items.remove(item)

    def get_throw_monkeys(self):
        return self.true_throw_monkey, self.false_throw_monkey
    
    def throw_item(self, item_tuple):
        """ Adds new item when an item is thrown """
        self.items.append(item_tuple)
    
    def operation(self, old_tuple):
        new_tuple = (0,0)
        multiplier, old = old_tuple[0], old_tuple[1]
        
        if self.operator == '+':
            """
            For Part 2, if operator is addition:
            Compute multiplication of multiplier and old.
            The new tuple's multiplier is set to 1
            """
            if self.op_value == "old":
                new_tuple = (1, (multiplier*old + multiplier*old))
            else:
                new_tuple = (1, (multiplier*old + int(self.op_value)))
        elif self.operator == '*':
            """
            For Part 2, if operator is multiply:
            No actual need to perform multiplication, 
            just return a tuple of a multiplier and the old value
            """

            if self.op_value == "old":
                new_tuple = (multiplier, old)
            else:
                new_tuple = (int(self.op_value), old)

        self.item_count += 1

        return new_tuple

    def check_divisibility(self, new_tuple):
        value = new_tuple[1]
        
        return value % self.div_check_val == 0

def get_data(is_part2=False):
    grid = None
    
    with open("day_11_data.txt") as f:
        monkeys = []  # List of monkey objects
        for line in f:
            line = line.strip()
            if line.startswith("Monkey"):
                items = []
                operator = ""
                op_value = 0
                div_check_val = 0
                true_throw_monkey = 0
                false_throw_monkey = 0
            
            elif line.startswith("Starting"):
                # Extract list of items
                items_string = line.split("Starting items: ")[1]
                items = items_string.split(', ')
                if is_part2:
                    # Convert to ints and initialise tuple with multiplier as 1
                    items = [(1,int(i)) for i in items]
                else:
                    items = [int(i) for i in items]  # Convert to ints
            
            elif line.startswith("Operation"):
                # Extract operator and operator value
                op_string = line.split("Operation: ")[1]
                formula = op_string.split()
                operator = formula[3]
                op_value = formula[4]
            
            elif line.startswith("Test"):
                # Extract divisibility test values
                div_check_val = int(line.split()[-1])
            
            elif line.startswith("If true"):
                # Extract true throw monkey
                true_throw_monkey = int(line.split()[-1])
            
            elif line.startswith("If false"):
                # Extract true throw monkey
                false_throw_monkey = int(line.split()[-1])
            else:
                if is_part2:
                    m_obj = Monkey2(items, operator, op_value, div_check_val, 
                                   true_throw_monkey, false_throw_monkey)
                else:
                    m_obj = Monkey(items, operator, op_value, div_check_val, 
                                   true_throw_monkey, false_throw_monkey)

                
                monkeys.append(m_obj)

    return monkeys


def part1(monkeys):
    for _ in range(20):
        for monkey_obj in monkeys:
            for i in monkey_obj.get_items().copy():
                new_item = monkey_obj.operation(i)
                
                # If divisible: monkey a, else: monkey b
                a, b = monkey_obj.get_throw_monkeys()

                # Throw new item to relevant monkey after checking divisibility
                if monkey_obj.check_divisibility(new_item):
                    monkeys[a].throw_item(new_item)
                else:
                    monkeys[b].throw_item(new_item)
                
                monkey_obj.remove_item(i)

    monkey_item_counts = [m_obj.get_item_count() for m_obj in monkeys]
    monkey_item_counts.sort(reverse=True)
    monkey_business = monkey_item_counts[0] * monkey_item_counts[1]

    print("Part 1:", monkey_business)
  

def part2(monkeys):
    for r in range(10_000):
        #print(f"\nR: {r+1}" + "#"*50)
        for m_i, monkey_obj in enumerate(monkeys):
            #print(f"\nMonkey {m_i}:")
            
            #print(f"Monkey items: {monkey_obj.get_items().copy()}:")
            for i_tuple in monkey_obj.get_items().copy():
                new_item_tuple = monkey_obj.operation(i_tuple)  # Operation tuple is initialised to multiple of 1 
               
                # If divisible: monkey a, else: monkey b
                a, b = monkey_obj.get_throw_monkeys()

                # Throw new item to relevant monkey after checking divisibility
                if monkey_obj.check_divisibility(new_item_tuple):
                    #print(f"\nMonkey inspecting: {i_tuple}")
                    #print(f"New tuple: {new_item_tuple} sent to {a}")
                    monkeys[a].throw_item(new_item_tuple)
                else:
                
                    #print(f"\nMonkey inspecting: {i_tuple}")
                    #print(f"New tuple: {new_item_tuple} sent to {b}")
                    monkeys[b].throw_item(new_item_tuple)
                
                monkey_obj.remove_item(i_tuple)

    monkey_item_counts = [m_obj.get_item_count() for m_obj in monkeys]
    
    #print(monkey_item_counts)
    monkey_item_counts.sort(reverse=True)

    monkey_business = monkey_item_counts[0] * monkey_item_counts[1]

    print("Part 2:", monkey_business)


monkeys = get_data()
part1(monkeys)

monkeys = get_data(is_part2=True)
part2(monkeys)