def reader():
    with open ('data9.txt') as inputFile:
        return list(map(int, (inputFile.read().splitlines())))
def twentyFiveNumCounter(tab):
    n = 25
    valid = False
    while n < len(tab):
        a = tab[(n-25):n]
        for x in a:
            if x!=tab[n]//2 and (tab[n]-x in set(a)):
                valid = True
                break
        if valid == False:
            return tab[n]
        valid = False
        n += 1
def setFinder(tab, invalid):
    m = 0
    for x in tab[m:]:
        list = [x]
        summ = x
        for i in tab[m+1:]:
            if (summ + i) < invalid:
                summ += i
                list.append(i)
            elif (summ + i) == invalid:
                list.append(i)
                return min(list) + max(list)
            else:
                m+=1
                break

list = reader()
invalid = twentyFiveNumCounter(list)
#first
print('Invalid number = ', invalid)
#second
print('Encryption weakness =', setFinder(list, invalid))