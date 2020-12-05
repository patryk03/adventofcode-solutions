tab = []
with open('czwarteDane.txt') as inputFile:
    tmpString = ""
    for x in inputFile:
        if x != "\n":
            tmpString += x
        else:
            tab.append(tmpString)
            tmpString = ""
    tab.append(tmpString)
list = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
def function(tab, list):
    wynik = 0
    for x in tab:
        isValid = True
        for i in list:
            if i not in x:
                isValid = False
                break
        if isValid:
            wynik+=1
    return wynik
print(function(tab, list))