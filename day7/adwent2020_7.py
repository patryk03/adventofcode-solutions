#def reader():
with open ("ddata.txt") as inputFile:
    tab = inputFile.read()
    print(tab)

for x in tab:
    print(x, end='')
#return dict([x.split('contain') for x in tab.split('\n')])

# def firstCounter():
#     bags = elements['shiny gold bags'].split(',')
#     print(bags)

#elements = reader()
#print(elements)
#firstCounter()
#reader()