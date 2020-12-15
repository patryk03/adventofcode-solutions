import copy
def reader():
    with open ('data11.txt') as inputFile:
        tab = inputFile.read().splitlines()
        return tab

def secondChangesCounter(tab, index, indexG):
    changes = False
    main = tab[indexG][index]
    num = 0
    tru = True
    if main != '.':
        for x in range(-1, 2):
            for i in range(-1, 2):
                g = copy.copy(x)
                c = copy.copy(i)
                while tru:
                    if (0<=(indexG+g) < len(tab)) and (0<=(index+c) < len(tab[0])):
                        if tab[indexG+g][index+c] == '#':
                            num +=1
                            break
                        elif tab[indexG+g][index+c] == 'L':
                            break
                    else:
                        break
                    if c < 0:
                        if g < 0:
                            g = g-1
                        elif g>0:
                            g+=1
                        c = c-1
                    elif c > 0:
                        c+=1
                        if g >0:
                            g+=1
                        elif g<0:
                            g-=1
                    elif c == 0:
                        if g <0:
                            g-=1
                        elif g>0:
                            g+=1
        if num == 0 and main == 'L':
            changes = True
            return changes, '#'
        elif num >= 6 and main == '#':
            changes = True
            return changes, 'L'
        return False, main
    else:
        return False, main

def changesCounter(tab, index, indexG):
    changes = False
    main = tab[indexG][index]
    num = 0
    for x in range(-1, 2):
        for i in range(-1, 2):
            if (0<=(indexG+x) < len(tab)) and (0<=(index+i) < len(tab[0])) and (tab[indexG+x][index+i] == '#'):
                num += 1
    if num == 0 and main == 'L':
        changes = True
        return changes, '#'
    elif num >= 5 and main == '#':
        changes = True
        return changes, 'L'
    return False, main
                
def checker(tab, which):
    changes = True
    while changes:
        changes = False
        secondTab = copy.deepcopy(tab)
        for x in range(len(tab)):
            for i in range(len(tab[x])):
                if which == 'first':
                    changeChange, doDodania = changesCounter(tab, i, x)
                else:
                    changeChange, doDodania = secondChangesCounter(tab, i, x)
                if changeChange == True:
                    changes = True
                secondTab[x][i] = doDodania
        tab = secondTab
    numOcc = 0
    for x in tab:
        for i in x:
            if i == '#':
                numOcc +=1
    return numOcc


tab = [list(x) for x in reader()] 

#first
print('first =', checker(tab, 'first'))

#second
print('second =', checker(tab, 'second'))