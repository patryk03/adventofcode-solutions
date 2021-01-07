import math

def reader():
    with open ('data20.txt') as input_file:
        input_file = input_file.read().split('\n\n')
        squares_list = {x.splitlines()[0]: x.splitlines()[1:] for x in input_file}
    return squares_list

def borders_options(squares_dict):
    borders_dict = {}
    second_borders_dict = {}
    for x in squares_dict:
        to_check = squares_dict[x]
        first_hori = to_check[0]
        second_hori = to_check[-1]
        left = ''
        right = ''
        for i in to_check:
            left += i[0]
            right += i[-1]
        borders_dict[x] = [first_hori, first_hori[::-1]], [second_hori, second_hori[::-1]], [left, left[::-1]], [right, right[::-1]]
        second_borders_dict[x] = first_hori, first_hori[::-1], second_hori, second_hori[::-1], left, left[::-1], right, right[::-1]
    return borders_dict, second_borders_dict

def edge_checker(borders, second_borders):
    to_return = []
    for x in borders:
        to_check = borders[x]
        num = 0
        for y in to_check:
            valid_border = False
            for c in y:
                for i in second_borders:
                    if x != i:
                        if c in second_borders[i]:
                            valid_border = True
                            break
            if valid_border:
                num +=1
        if num == 2:
            to_return.append(x)
    return math.prod(list(map(int, [x.split(' ')[1].replace(':', '') for x in to_return])))

        




squares_dict = reader()
borders, second_tab = borders_options(squares_dict)
edges_list = edge_checker(borders, second_tab)
#first
print(edges_list)

