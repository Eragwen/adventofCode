#dayThree Part One
import string

value = list(string.ascii_lowercase) + list(string.ascii_uppercase)

res = []

with open("src/puzzle3.txt") as f:
    data = f.read().splitlines()

for i in data:
    p1, p2 = i[:len(i)//2], i[len(i)//2:]
    res.append(value.index(list(set(p1) & set(p2))[0])+1)

print(sum(res))
res.clear()

#dayThree Part Two

for i in range(0, len(data), 3):
    dataTrip = set(data[i])& set(data[i+1])& set(data[i+2])
    res.append(value.index(list(dataTrip)[0])+1)

print(sum(res))