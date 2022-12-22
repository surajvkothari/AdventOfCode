# Advent of code 2019
# Day 2

def restData():
    data = []
    with open("data.txt") as f:
        dataSplit = f.read().split(",")
        data = [int(i) for i in dataSplit]
    return data


""" Part 1 """
def Intcode(code, pointer):
    while True:
        if code[pointer] == 1:
            code[code[pointer+3]] = code[code[pointer+1]] + code[code[pointer+2]]
            pointer += 4

        elif code[pointer] == 2:
            code[code[pointer+3]] = code[code[pointer+1]] * code[code[pointer+2]]
            pointer += 4

        elif code[pointer] == 99:
            return code

data = restData()
data[1] = 12
data[2] = 2
print(Intcode(data, 0)[0])

""" Part 2 """
for noun in range(100):
    for verb in range(100):
        data = restData()

        data[1] = noun
        data[2] = verb

        result = Intcode(data, 0)[0]
        if result == 19690720:
            end = True

            print(100 * noun + verb)
            break
