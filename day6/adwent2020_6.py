def reader():
    tab = []
    with open("data6.txt") as inputFile:
        tab = inputFile.read() 
    return tab.replace("\n\n", "|").replace('\n','&')

def ansCounter(x):
    tmpTab = []
    for i in x:
        if i not in tmpTab:
            tmpTab.append(i)
    return len(tmpTab)

def groupTester(listToChange):
    result = 0
    ansList = listToChange.replace('&', '').split('|')
    for x in ansList:
        result += ansCounter(x)
    return result

def dictionaryTesting(x):
    dict = {}
    length = len(x)
    result = 0
    for i in x:
        for m in i:
            if m in dict:
                dict[m] +=1
            else:
                dict[m] = 1
    for n in dict.values():
        if n == length:
            result +=1
    return result

def everyoneAns(listToChange):
    ansList = listToChange.split('|')
    toReturn = 0
    for x in ansList:
        toReturn += dictionaryTesting(x.split('&'))
    return toReturn

listToChange = reader()
#first
print("first =", groupTester(listToChange))
#second
print("second = ", everyoneAns(listToChange))