def restData():
    data = []
    with open("data.txt") as f:
        dataSplit = f.read().split(",")
        data = [int(i) for i in dataSplit]
    return data

""" Part 1 """
def addPadding(opcode):
    if len(opcode) == 3:
        opcode = "00" + opcode
    elif len(opcode) == 4:
        opcode = "0" + opcode

    return opcode

def applyMode(mode, code, pointer):
    if mode == "0":
        return code[code[pointer]]
    else:
        return code[pointer]

def Intcode(code, pointer):
    while True:
        if code[pointer] == 1:
            code[code[pointer+3]] = code[code[pointer+1]] + code[code[pointer+2]]
            pointer += 4

        elif code[pointer] == 2:
            code[code[pointer+3]] = code[code[pointer+1]] * code[code[pointer+2]]
            pointer += 4

        elif code[pointer] == 3:
            val = int(input(">> "))
            code[code[pointer+1]] = val
            pointer += 2

        elif code[pointer] == 4:
            print(code[code[pointer+1]])
            pointer += 2

        elif len(str(code[pointer])) > 1:
            opcode = addPadding(str(code[pointer]))
            if opcode[3:5] == "01":
                modeA, modeB, modeC = opcode[0], opcode[1], opcode[2]
                if modeA == "0":
                    code[code[pointer+3]] = applyMode(modeC, code, pointer+1) + applyMode(modeB, code, pointer+2)
                else:
                    code[pointer+3] = applyMode(modeC, code, pointer+1) + applyMode(modeB, code, pointer+2)

                pointer += 4

            elif opcode[3:5] == "02":
                modeA, modeB, modeC = opcode[0], opcode[1], opcode[2]
                if modeA == "0":
                    code[code[pointer+3]] = applyMode(modeC, code, pointer+1) * applyMode(modeB, code, pointer+2)
                else:
                    code[pointer+3] = applyMode(modeC, code, pointer+1) * applyMode(modeB, code, pointer+2)

                pointer += 4

            elif opcode[3:5] == "03":
                modeC = opcode[2]
                val = int(input(">> "))
                if modeA == "0":
                    code[code[pointer+3]] = val
                else:
                    code[pointer+3] = val

                pointer += 2

            elif opcode[3:5] == "04":
                modeC = opcode[2]
                if modeA == "0":
                    print(code[code[pointer+3]])
                else:
                    print(code[pointer+3])
                
                pointer += 2

            elif opcode[3:5] == "99":
                return code

        elif code[pointer] == 99:
            return code

data = restData()
Intcode(data, 0)
