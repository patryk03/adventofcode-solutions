def fileReader():
    tab = []
    with open ("piateDane.txt") as inputFile:
        tab = inputFile.readlines()
    return tab

def binary(upper, moves, range, char):
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
            return cent

def myId(results):
    old = results[0]
    for x in results[1:]:
        if x != old+1:
            return x-1
        old = x

def counter(moves):
    results = []
    for x in moves:
        resultOne = binary(127, x[:7], 7, "F")
        resultTwo = binary(7, x[7:], 3, "L")
        results.append(resultOne * 8 + resultTwo)
    return results

moves = fileReader()
results = counter(moves)

#first

print("Max = ", max(results))

#second

print("My id = ", myId(sorted(results)))