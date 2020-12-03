with open('trzecieDane.txt') as inputFile:
    tab = inputFile.readlines()
move = 0
wynik = 0
for x in tab:
    string = x.strip()
    position = move%len(string)
    object = string[position]
    if object == "#":
        wynik +=1
    move +=3
print(wynik)