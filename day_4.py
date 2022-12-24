#dayFour Part One

cpt = 0
res = []

with open('src/puzzle_4.txt') as f:
    lines = f.read().split("\n")

def get_num(pair):
    p1, p2 = pair.split("-")
    return int(p1), int(p2)

for line in lines:
    firstPair, secondPair = line.split(",")
    firstId, secondId = get_num(firstPair)
    thirdId, fourthId = get_num(secondPair)
    if firstId <= thirdId and fourthId<= secondId or thirdId <= firstId and secondId <= fourthId:
        cpt += 1
        res.append(line)

print(res)
print(cpt)
cpt = 0

#dayFour Part Two

for line in lines:
    firstPair, secondPair = line.split(",")
    firstId, secondId = get_num(firstPair)
    thirdId, fourthId = get_num(secondPair)
    if firstId > fourthId or thirdId > secondId:
        res.append(line)
    else:
        cpt += 1
print(cpt)