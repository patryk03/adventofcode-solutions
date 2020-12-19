import copy
def reader():
    with open ('data14.txt') as inputFile:
        tabToCheck = []
        tab = inputFile.read().replace('mask = ', '', 1).split('mask = ')
        tab = [x.split('\n') for x in tab]
        for i in tab:
            mask = i[0]
            locations = [(x.split(' = ')[0].replace('mem[', ']').replace(']', ''), x.split(' = ')[1]) for x in i[1:] if x != '']
            tabToCheck.append((mask, locations))
    return tabToCheck

def maskDecoder(mask):
    whereToChange = {}
    for x in range(len(mask)):
        if mask[x] == '0':
            whereToChange[x] = '0'
        elif mask[x] == '1':
            whereToChange[x] = '1'
    return whereToChange


def memorySpaceFinder(mask, locations, memorySpaces):
    changes = maskDecoder(mask)
    for x in locations:
        adress = x[0]
        decimalValue = int(x[1])
        binValue = list(format(decimalValue, '036b'))
        for a in changes:
            index = a
            value = changes[a]
            binValue[index] = value
        binValue = "".join(binValue)
        decimalValue = int(binValue, 2)
        memorySpaces[adress] = decimalValue
    return memorySpaces


def adressDecoder(mask):
    mask = mask[::-1]
    whereToChange = {}
    for x in range(len(mask)):
        if mask[x] == 'X':
            whereToChange[x] = 'X'
        elif mask[x] == '1':
            whereToChange[x] = '1'
    return whereToChange

def adressSpaceFinder(mask, locations, memorySpaces):
    changes = adressDecoder(mask)
    for x in locations:
        addToAdress = [0]
        decimalAdress = int(x[0])
        valueFirst = int(x[1])
        binAdress = list(format(decimalAdress, '036b'))[::-1]
        for a in changes:
            index = a
            value = changes[a]
            if value != 'X':
                binAdress[index] = value
            else:
                binNumber = 2**index
                adress = copy.deepcopy(addToAdress)
                for i in adress:
                    addToAdress.append(i + binNumber)
                binAdress[index] = '0'
        binAdress = "".join(binAdress[::-1])
        decimalAdress = int(binAdress, 2)
        for n in addToAdress:
            memorySpaces[decimalAdress + n] = valueFirst
    return memorySpaces


tabToCheck = reader()

#first
memorySpaces = {}
for x in tabToCheck:
    memorySpaces = memorySpaceFinder(x[0], x[1], memorySpaces)
print('first =', sum(memorySpaces.values()))

#second
memorySpaces = {}
for x in tabToCheck:
    memorySpaces = adressSpaceFinder(x[0], x[1], memorySpaces)
print('second =', sum(memorySpaces.values()))