from copy import deepcopy

def reader():
    with open ("data8.txt") as inputFile:
       tab = inputFile.read().splitlines()
    return tab

def wayFinder(list):
    i = 0
    tab = []
    accumulator = 0
    while i not in tab:
        tab.append(i)
        key, value = list[i]
        if key == "nop":
            i+=1
        elif key == "acc":
            accumulator+=int(value)
            i+=1
        else:
            i+=int(value)
        if i == len(list):
            return accumulator, True
    return accumulator, False
def problemResolver(list):
    for x in range(len(list)):
        alternativeTab = deepcopy(list)
        if list[x][0] == "jmp":
            alternativeTab[x][0] = "nop"
        elif list[x][0] == "nop":
            alternativeTab[x][0] = "jmp"
        ans, condition = wayFinder(alternativeTab)
        if condition:
            return ans

mainList = [x.split(" ") for x in reader()]
#first
print("first = ", wayFinder(mainList)[0])
#second
print("second = ", problemResolver(mainList))