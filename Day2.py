def restData():
    data = []
    with open("data.txt") as f:
        dataSplit = f.read().split(",")
        data = [int(i) for i in dataSplit]
    return data


""" Part 1 """
def Intcode(code, opcode):
    while True:
        if code[opcode] == 1:
            code[code[opcode+3]] = code[code[opcode+1]] + code[code[opcode+2]]

            opcode += 4
        elif code[opcode] == 2:
            code[code[opcode+3]] = code[code[opcode+1]] * code[code[opcode+2]]
            opcode += 4
        elif code[opcode] == 99:
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
