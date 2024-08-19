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
         
        new = int(new / 3)  # Always divide by 3 after operation

        self.item_count += 1

        return new

    def check_divisibility(self, new):
        return new % self.div_check_val == 0


def get_data():
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
                m_obj = Monkey(items, operator, op_value, div_check_val, 
                            true_throw_monkey, false_throw_monkey)
                
                monkeys.append(m_obj)

    return monkeys


def part1(monkeys):
    for r in range(20):
        for m_id, monkey_obj in enumerate(monkeys):
            for i in monkey_obj.get_items().copy():
                #print(f"\nMonkey inspects: {i}")
                new_item = monkey_obj.operation(i)
                #print(f"New item: {new_item}")
                
                # If divisible: monkey a, else: monkey b
                a, b = monkey_obj.get_throw_monkeys()

                # Throw new item to relevant monkey after checking divisibility
                if monkey_obj.check_divisibility(new_item):
                    #print(f"New item thrown to monkey: {a}")
                    monkeys[a].throw_item(new_item)
                else:
                    #print(f"New item thrown to monkey: {b}")
                    monkeys[b].throw_item(new_item)
                
                monkey_obj.remove_item(i)

    monkey_item_counts = [m_obj.get_item_count() for m_obj in monkeys]
    monkey_item_counts.sort(reverse=True)
    monkey_business = monkey_item_counts[0] * monkey_item_counts[1]

    print("Part 1:", monkey_business)
  

def part2(monkeys):
    for r in range(1):
        for m_zd, monkey_obj in enumerate(monkeys):
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
    print(monkey_item_counts)

    monkey_business = monkey_item_counts[0] * monkey_item_counts[1]

    print("Part 2:", monkey_business)


monkeys = get_data()
part1(monkeys)

monkeys = get_data()
#part2(monkeys)