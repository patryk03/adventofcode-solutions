tab = []
with open('.\pierwszeDane.txt') as inputFile:
    for line in inputFile:
        tab.append(line)
tab = list(map(int, tab))
for x in tab:
    if 2020-x in set(tab):
        print(x*(2020-x))
        exit()