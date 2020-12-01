tab = []
with open('.\pierwszeDane.txt') as inputFile:
    for line in inputFile:
        tab.append(line)
tab = list(map(int, tab))
tab = sorted(tab)
for x in tab:
    for i in tab:
        for n in tab:
            if x+i+n == 2020:
                print(x*i*n)
                exit()
            elif x+i+n >2020:
                break