def reader():
    with open ('data13_1.txt') as inputFile:
        tab = inputFile.read().splitlines()
        tab[1] = [x for x in tab[1].replace('x', "").split(",") if x != '']
    return tab

def secondReader():
    with open ('data13_2.txt') as inputFile:
        tab = inputFile.read()
        tab = tab.split(',')
    return tab

def closestFinder(tab):
    toFind = int(tab[0])
    bestId = 0
    bestTime = 1000000000
    for x in tab[1]:
        g = round(toFind/x, 0)
        c = g*x
        if c >= toFind:
            time = x - (toFind%x)
            if time < bestTime:
                bestTime = time
                bestId = x
        else:
            u = c +x
            time = u%toFind
            if time < bestTime:
                bestTime = time
                bestId = x
    return bestId, bestTime

def secondTimestamp(tab):
    mainDep = tab[0]
    i = 0
    while 1:
        delay = 1
        depToCheck = int(mainDep) *i
        for x in range(len(tab[1:])):
            if tab[x+1] == 'x':
                delay+=1
            else:
                g = int(tab[x+1])
                c = depToCheck + delay
                if (depToCheck +delay)%g == 0:
                    if x == (len(tab)-2):
                        return depToCheck
                    delay +=1
                else:
                    break
        i +=1



tab = reader()
tab[1] = list(map(int, tab[1]))


#first
a,b = closestFinder(tab)
print('first =', a*b)

#second
secondTab = secondReader()
print(secondTimestamp(secondTab))
