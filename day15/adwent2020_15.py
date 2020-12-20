def reader():
    with open ('data15.txt') as inputFile:
        return {i:x+1 for x, i in enumerate(inputFile.read().split(','))}

def turns(listOfTurns, range):
    num = len(listOfTurns)+1
    toAdd = '0'
    toCheck = '0'
    while num != range:
        if toCheck in listOfTurns:
            toCheck = str(num - listOfTurns[toCheck])
        else:
            toCheck = '0'
        listOfTurns[toAdd] = num
        toAdd = toCheck
        num +=1
    return toAdd

listOfTurns = reader()
#first
print('first =', turns(listOfTurns, 2020))

listOfTurns = reader()
#second
print('second =', turns(listOfTurns, 30000000))