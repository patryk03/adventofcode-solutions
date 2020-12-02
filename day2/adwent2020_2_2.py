tab = []
wynik = 0
with open('.\drugieDane.txt') as inputFile:
    tab = inputFile.readlines()
for x in tab:
    string = x.split(" ")
    positions = string[0].split("-")
    positions = list(map(int, positions))
    positions = [x-1 for x in positions]
    letter = string[1][0]
    if (string[2][positions[0]] == letter and string[2][positions[1]] != letter) or (string[2][positions[1]] == letter and string[2][positions[0]] != letter):
        wynik +=1
print(wynik)