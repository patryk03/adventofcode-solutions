tab = []
list = [(1920, 2002), (2010, 2020), (2020, 2030)]
letters = ["a","b","c","d","e","f",]
ints = ["0","1","2","3","4","5","6","7","8","9"]
color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
with open('czwarteDane.txt') as inputFile:
    tmpTab = []
    for x in inputFile:
        if x != "\n":
            tmpTab.extend(x.strip().split(" "))
        else:
            tab.append(sorted(tmpTab))
            tmpTab = []
    tab.append(sorted(tmpTab))
def second(tab, list, letters, ints, color):
    wynik = 0
    for x in tab:
        isValid = 0
        if len(x) >= 7:
            for i in range(len(x)):
                data = x[i].split(":")
                if ((data[0] == "byr") and (list[0][0] <= int(data[1]) and int(data[1]) <= list[0][1])) or((data[0] == "iyr") and (list[1][0] <= int(data[1]) and int(data[1]) <= list[1][1]))  or ((data[0] == "eyr") and (list[2][0] <= int(data[1]) and int(data[1]) <= list[2][1])):
                    isValid +=1
                elif data[0] == "hgt":
                    if "cm" in data[1]:
                        a = True
                        try:
                            int(data[1][:3])
                        except ValueError:
                            a = False
                        if a == True and 150 <= int(data[1][:3]) and int(data[1][:3]) <= 193:
                            isValid +=1
                    elif "in" in data[1]:
                        a = True
                        try:
                            int(data[1][:2])
                        except ValueError:
                            a = False
                        if a == True and 59 <= int(data[1][:2]) and int(data[1][:2]) <= 76:
                            isValid+=1
                elif data[0] == "hcl":
                    if data[1][0] == "#":
                        test = True 
                        for n in range(1, len(data[1])):
                            if (data[1][n] not in letters) and (data[1][n] not in ints):
                                test = False
                        if test == True:
                            isValid +=1
                elif data[0] == "ecl":
                    if data[1] in color:
                        isValid +=1
                elif data[0] == "pid":
                    if len(data[1]) == 9:
                        isValid+=1
                if isValid == 7:
                    wynik +=1
                    break
    return wynik
print(second(tab, list, letters, ints, color))
            
