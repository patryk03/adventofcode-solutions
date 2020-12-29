def reader():
    with open ('data17.txt') as inputFile:
        tab = inputFile.read().splitlines()
        z = 0
        toReturn = set()
        for x in range(len(tab)):
            for i, m in enumerate(tab[x]):
                if m == '#':
                    toReturn.add((i, x, z))
    return toReturn

def secondReader():
    with open ('data17.txt') as inputFile:
        tab = inputFile.read().splitlines()
        z = 0
        w = 0
        toReturn = set()
        for x in range(len(tab)):
            for i, m in enumerate(tab[x]):
                if m == '#':
                    toReturn.add((i, x, z, w))
    return toReturn

def neighbours(coordinates, positions):
    num = 0
    inactives = []
    for cX in [-1, 0, 1]:
        for cY in [-1, 0, 1]:
            for cZ in [-1, 0, 1]:
                if cX == cY == cZ == 0:
                    pass
                else:
                    a = (coordinates[0]+cX, coordinates[1]+cY, coordinates[2]+cZ)
                    if a in positions:
                        num +=1
                    else:
                        inactives.append(a)
    if num == 2 or num == 3:
        return True, inactives
    return False, inactives

def secondNeighbours(coordinates, positions):
    num = 0
    inactives = []
    for cX in [-1, 0, 1]:
        for cY in [-1, 0, 1]:
            for cZ in [-1, 0, 1]:
                for cW in [-1, 0, 1]:
                    if cX == cY == cZ == cW == 0:
                        pass
                    else:
                        a = (coordinates[0]+cX, coordinates[1]+cY, coordinates[2]+cZ, coordinates[3]+cW)
                        if a in positions:
                            num +=1
                        else:
                            inactives.append(a)
    if num == 2 or num == 3:
        return True, inactives
    return False, inactives

def cycles(positions, change):
    cyclesNum = 0
    while cyclesNum < 6:
        newPositions = set()
        positionsToCheck = {}
        for x in positions:
            if change == 1:
                isActive, inactives = neighbours(x, positions)
            else:
                isActive, inactives = secondNeighbours(x, positions)
            if isActive == True:
                newPositions.add(x)
            for i in inactives:
                listToTuple = i
                if listToTuple in positionsToCheck:
                    positionsToCheck[listToTuple] +=1
                else:
                    positionsToCheck[listToTuple] = 1
        for m in positionsToCheck:
            if positionsToCheck[m] == 3:
                newPositions.add(m)
        positions = newPositions
        cyclesNum +=1
    return len(positions)


#first
print('first =', cycles(reader(), 1))

#second
print('second =', cycles(secondReader(), 2))