
import copy
from collections import defaultdict
from os import remove
def reader():
    with open ('data16.txt') as inputFile:
        rules = set()
        nearbyTickets = []
        tab = inputFile.read().split('\n\n')
        toChange = [x.split(': ')[1].split(' or ') for x in tab[0].split('\n')]
        for x in toChange:
            for i in x:
                k = i.split("-")
                k = list(map(int, k))
                for c in range(k[0], k[1]+1):
                    rules.add(c)
        nearbyTickets = [x.split(',') for x in tab[2][16:].split('\n')]
        nearbyTickets = [list(map(int, x)) for x in nearbyTickets]
        return rules, nearbyTickets

def secondReader():
    with open ('data16.txt') as inputFile:
        rules = dict()
        tab = inputFile.read().split('\n\n')
        toChange = [x.split(': ')[1].split(' or ') for x in tab[0].split('\n')]
        for x, m in enumerate(toChange):
            tmpTab = set()
            for i in m:
                k = i.split("-")
                k = list(map(int, k))
                for c in range(k[0], k[1]+1):
                    tmpTab.add(c)
            rules[x] = tmpTab
        myTicket = list(map(int, tab[1][13:].split(',')))
        return rules, myTicket
    
def rulesChecker(rules, nearbyTickets):
    ans = 0
    toReturn = copy.deepcopy(nearbyTickets)
    for x in range(len(nearbyTickets)):
        for i in nearbyTickets[x]:
            if i not in rules:
                toReturn[x].remove(i)
                ans+=i
    return ans, toReturn

def rightOrder(optionsDict):
    whatToDel = set()
    toReturn = {}
    x = 0
    while len(toReturn) <= len(optionsDict):
        if (len(optionsDict[x])) == 1:
            whatToDel.add(list(optionsDict[x])[0])
            toReturn[x] = list(optionsDict[x])[0]
            del optionsDict[x]
        else:
            for i in whatToDel:
                if i in optionsDict[x]:
                    optionsDict[x].remove(i)
        x = (x+1)%len(optionsDict)
    return toReturn

def myTicketValues(rules, myTicket):
    firstSent = set(range(0,6))
    whichList = []
    toReturn = 1
    for x in rules:
        if rules[x] in firstSent:
            whichList.append(x)
    for i in whichList:
        toReturn = toReturn * myTicket[i]
    return toReturn

def secondRulesChecker(rules, nearbyTickets, myTicket):
    optionsDict = defaultdict(set)
    for x in nearbyTickets:
        for i in range(len(x)):
            tmpSet = set()
            for n in rules:
                if x[i] in rules[n]:
                    tmpSet.add(n)
            if i in optionsDict:
                c = optionsDict[i].intersection(tmpSet)
                optionsDict[i] = c
            else:
                optionsDict[i] = tmpSet
    return myTicketValues(rightOrder(optionsDict), myTicket)

# first
rules, nearbyTickets = reader()
ans, nearbyTickets = rulesChecker(rules, nearbyTickets)
print('first =', ans)

# second
rules, myTicket = secondReader()
print('second =', secondRulesChecker(rules, nearbyTickets, myTicket))