#dayTwo Part 1

Pos ={
"A" : {"X":3, "Y":6, "Z":0},
"B" : {"X":0, "Y":3, "Z":6},
"C" : {"X":6, "Y":0, "Z":3},
}
Pts = {
"X" : 1,
"Y" : 2,
"Z" : 3,
}
score = 0
with open("src/puzzle_2.txt",'r') as i:
    total = i.read().split("\n")

for line in total:
    opponent, me = line.split(" ")
    score += Pos[opponent][me] + Pts[me]

print("Score: " + str(score))

#dayTwo Part 2

Pos ={
    "A": {"lose": 'Z', "draw": 'X', "win": 'Y'},
    "B": {"lose": 'X', "draw": 'Y', "win": 'Z'},
    "C": {"lose": 'Y', "draw": 'Z', "win": 'X'}
}
Pts = {"X" : 1,"Y" : 2,"Z" : 3}
score = 0
Strat = {"X": "lose", "Y":"draw", "Z":"win"}

with open("src/puzzle_2.txt",'r') as i:
    game = i.read().split("\n")

for line in game:
    opponent, me = line.split(" ")
    if Strat[me] == "win":
        rightP = Pos[opponent]["win"]
        score += 6 + Pts[rightP]
    elif Strat[me] == "draw":
        rightP = Pos[opponent]["draw"]
        score += 3 + Pts[rightP]
    elif Strat[me] == "lose":
        rightP = Pos[opponent]["lose"]
        score += 0 + Pts[rightP]

print("Score : "+ str(score))