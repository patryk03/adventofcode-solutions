tab = []
with open('.\pierwszeDane.txt') as inputFile:
    for line in inputFile:
        tab.append(line)
tab = list(map(int, tab))
tab = sorted(tab)
drugiTab = tab[::-1]
for x in tab:
    for i in drugiTab:
        if x+i == 2020:
            print(x*i)
            exit()
        elif i == x:
            break