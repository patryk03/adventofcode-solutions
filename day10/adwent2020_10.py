def reader():
    with open ('data10.txt') as inputFile:
        return list(map(int, (inputFile.read().splitlines())))

def pathFinder(tab):
    num = 0
    oneDistance = 0
    threeDistance = 0
    toFind = max(tab) +3
    searchingSet = set(tab)
    while num != toFind:
        if num+1 in searchingSet:
            oneDistance+=1
            num +=1
        elif num+2 in searchingSet:
            num+=2
        else:
            threeDistance+=1
            num+=3
    return (oneDistance*threeDistance)

def checkPossibilities(oneDistanceCounter, distance):
    if (oneDistanceCounter == -1 and distance == 3):
        return 0
    elif oneDistanceCounter <=1:
        return 1
    return checkPossibilities(oneDistanceCounter-1, 1) + checkPossibilities(oneDistanceCounter-2,2) + checkPossibilities(oneDistanceCounter-3,3)

def diffrentWays(tab):
    num = 0
    possibilities = 1
    oneDistanceCounter = 0
    toFind = max(tab) +3
    searchingSet = set(tab)
    while num != toFind:
        if num+1 in searchingSet:
            oneDistanceCounter +=1
            num +=1
        else:
            multiplier = checkPossibilities(oneDistanceCounter, 0)
            possibilities = possibilities * multiplier
            oneDistanceCounter = 0
            num+=3
    return possibilities * checkPossibilities(oneDistanceCounter, 0)

tab = reader()

#first
print('first =', pathFinder(tab))

#second
print('second =', diffrentWays(tab))