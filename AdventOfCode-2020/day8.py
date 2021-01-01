# Advent of code 2020
# Day 8

""" Part 1 """

# Gets instructions
def get_instructions():
    with open("day8_data.txt") as f:
        instruction_set = [i.strip().split() for i in f]

    return instruction_set

def parse_instructions(instruction_set):
    ACCUMULATOR = 0
    instruction_pointer = 0
    instructions_visited = []

    while True:
        if instruction_pointer < len(instruction_set):
            instruction = instruction_set[instruction_pointer]
            if instruction_pointer in instructions_visited:
                return (False, ACCUMULATOR) # Return false to indicate infinite loop
            else:
                instructions_visited.append(instruction_pointer)

                opcode = instruction[0]
                operand = int(instruction[1])

                if opcode == "acc":
                    # Increase or decrease accumulator
                    ACCUMULATOR += operand
                    instruction_pointer += 1
                elif opcode == "jmp":
                    # Change instruction pointer
                    instruction_pointer += operand
                elif opcode == "nop":
                    # Do nothing
                    instruction_pointer += 1
        else:
            return (True, ACCUMULATOR) # Return true to indicate succesful ending


instruction_set = get_instructions()
ended, acc = parse_instructions(instruction_set)
print("Accumulator (Part 1):", acc)

""" Part 2 """
ended = False
instruction_change_pointer = 0
while not ended:
    instruction_set_copy = get_instructions() # Make a copy of the original instruction set

    operand = instruction_set_copy[instruction_change_pointer][0]

    if operand == "nop":
        instruction_set_copy[instruction_change_pointer][0] = "jmp"
    elif operand == "jmp":
        instruction_set_copy[instruction_change_pointer][0] = "nop"


    ended, acc = parse_instructions(instruction_set_copy) # Will return true if ended
    instruction_change_pointer += 1


print("Accumulator (Part 2):", acc)
