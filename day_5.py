import re

tab=[['Z', 'J', 'N', 'W', 'P', 'S'], ['G', 'S', 'T'], ['V', 'Q', 'R', 'L', 'H'], 
['V', 'S', 'T', 'D'], ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'], 
['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'], ['L', 'P', 'M', 'W', 'G', 'T', 'J'], 
['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'], ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']]

with open("src/puzzle_5.txt", "r") as f:
    lines = f.read().split("\n")

pattern = r'\d+'
instructions = []

for line in lines:
    num = re.findall(pattern, line)
    instructions.append(num)
print(tab)

print("================================")

for instruction in instructions:
    tab_transitor = []
    nb_element = int(instruction[0])
    colonne_envoi = int(instruction[1])-1
    colonne_reception = int(instruction[2])-1
    for i in range (nb_element):
        if tab[colonne_envoi] != []:
            add = tab[colonne_envoi].pop()
            tab_transitor.append(add)
    tab_transitor.reverse()
    for j in range(len(tab_transitor)):
        tab[colonne_reception].append(tab_transitor[j])

print(tab)

