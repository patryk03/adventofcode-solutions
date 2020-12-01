tab = []
with open('.\pierwszeDane.txt') as inputFile:
    tab = inputFile.readlines()
tab = list(map(int, tab))
for x in tab:
    for i in tab:
        if 2020-(x+i) in set(tab):
            print(x*i*(2020-(x+i)))
            exit()