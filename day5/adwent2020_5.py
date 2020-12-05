def fileReader():
    tab = []
    with open ("piateDane.txt") as inputFile:
        tab = inputFile.readlines()
    return tab

def binary(upper, moves, range, char, allMoves):
    num = 0
    lower = 0
    cent = 0
    for i in moves:
        cent = (lower+upper)//2
        if i == char:
            upper = cent
        else:
            lower = cent+1
            cent = lower
        num+=1
        if num == range:
            if range == 3:
                return cent
            else:
                otherNumber = binary(7, allMoves[7:], 3, "L", allMoves)
                return (cent*8 + otherNumber)

def myId(results):
    old = results[0]
    for x in results[1:]:
        if x != old+1:
            return x-1
        old = x

results = []
moves = fileReader()
for x in moves:
    results.append(binary(127, x[:7], 7, "F", x))

#first
print("Max = ", max(results))
#second
print("My id = ", myId(sorted(results)))