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
        if num+2 in searchingSet:
            num+=2
        if num+3 in searchingSet:
            threeDistance+=1
            num+=3
    return (oneDistance*threeDistance)


tab = reader()
#first
print(pathFinder(tab))