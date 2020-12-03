with open('trzecieDane.txt') as inputFile:
    tab = inputFile.readlines()
moveOne = [0,0]
moveTwo = [0,0]
moveThree = [0,0]
moveFour = [0,0]
moveFive = [0,0]
itteration = 0
for x in tab:
    string = x.strip()
    if string[moveOne[0]%len(string)] == "#":
        moveOne[1] += 1
    if string[moveTwo[0]%len(string)] == "#":
        moveTwo[1] +=1
    if string[moveThree[0]%len(string)] == "#":
        moveThree[1] +=1
    if string[moveFour[0]%len(string)] == "#":
        moveFour[1] +=1
    if itteration %2 == 0:
        if string[moveFive[0]%len(string)] == "#":
            moveFive[1] +=1
        moveFive[0] +=1
    moveOne[0] +=1
    moveTwo[0] +=3
    moveThree[0] +=5
    moveFour[0] +=7
    itteration +=1
print(moveOne[1] * moveTwo[1] * moveThree[1] * moveFour[1] * moveFive[1])