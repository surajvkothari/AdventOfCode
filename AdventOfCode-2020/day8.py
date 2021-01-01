# Advent of code 2020
# Day 8

""" Part 1 """

# Gets instructions
#instruction_set = []
with open("day8_data.txt") as f:
    instruction_set = [i.strip().split() for i in f]

def parse_instructions(instruction_set):
    ACCUMULATOR = 0
    instruction_pointer = 0
    instructions_visited = []

    while True:
        instruction = instruction_set[instruction_pointer]
        if instruction_pointer in instructions_visited:
            print("Acumulator:",ACCUMULATOR)
            break # Exit, otherwise infinite loop will occur
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

parse_instructions(instruction_set)
