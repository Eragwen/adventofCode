#dayOne Part 1

print(max(sum(list(map(int, i.split("\n")))) for i in open("src/puzzle1.txt",'r').read().split("\n\n")[:-1]))

#dayOne Part 2

print(sum(sorted((sum(list(map(int, i.split("\n")))) for i in open("src/puzzle1.txt",'r').read().split("\n\n")[:-1]))[-3:]))
