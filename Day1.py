def calcFuel(m):
    return int(m / 3) - 2

data = []
with open("data.txt") as f:
    for line in f:
        data.append(int(line.strip("\n")))

#print(data)

fuel = [calcFuel(i) for i in data]
print(sum(fuel))
