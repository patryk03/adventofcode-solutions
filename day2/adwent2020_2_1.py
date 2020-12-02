tab = []
wynik = 0
with open('.\drugieDane.txt') as inputFile:
    tab = inputFile.readlines()
for x in tab:
    string = x.split(" ")
    range = string[0].split("-")
    letter = string[1][0]
    number = string[2].count(letter)
    if number >= int(range[0]) and number <= int(range[1]):
        wynik +=1
print(wynik)