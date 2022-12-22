# Advent of code 2019
# Day 1

data = []
with open("data.txt") as f:
    for line in f:
        data.append(int(line.strip("\n")))


""" Part 1 """
def calcFuel(mass):
    return int(mass / 3) - 2

fuel = [calcFuel(m) for m in data]

""" Part 2 """
def recursiveFuel(mass, mTotal):
    mTemp = int(mass / 3) - 2
    if mTemp <= 0:
        return mTotal
    else:
        mTotal += mTemp
        return recursiveFuel(mTemp, mTotal)

def calcTotalFuel(mass):
    Total = 0
    Total = recursiveFuel(mass, Total)
    return Total

fuel2 = [calcTotalFuel(m) for m in data]
print(sum(fuel2))
