def reader():
    with open ('data18.txt') as input_file:
        return [x.replace(' ', '') for x in input_file.read().splitlines()]

def convert_to_ONP_first(tab):
    converted_tab = []
    for x in tab:
        stack = []
        tmp_tab = []
        for i in range(len(x)):
            operator = x[i]
            if operator == '+' or operator == '*':
                if len(stack) != 0:
                    last_operator = stack[-1]
                    if (operator == '*' or operator == '+') and last_operator != '(':
                        a = stack.pop()
                        tmp_tab.append(a)
                        stack.append(operator)
                    else:
                        stack.append(operator)
                else:
                    stack.append(operator)
            elif operator == '(':
                stack.append(operator)
            elif operator == ')':
                m = len(stack)-1
                while stack[m] != '(':
                    a = stack.pop()
                    tmp_tab.append(a)
                    m-=1
                stack.pop()
            else:
                tmp_tab.append(x[i])
        while 1:
            try:
                a = stack.pop()
                tmp_tab.append(a)
            except:
                converted_tab.append(tmp_tab)
                break
    return converted_tab

def convert_to_ONP_second(tab):
    converted_tab = []
    for x in tab:
        stack = []
        tmp_tab = []
        for i in range(len(x)):
            operator = x[i]
            if operator == '+' or operator == '*':
                if len(stack) != 0:
                    last_operator = stack[-1]
                    if (operator == last_operator) or (operator == '*' and last_operator == '+'):
                        a = stack.pop()
                        tmp_tab.append(a)
                        stack.append(operator)
                    else:
                        stack.append(operator)
                else:
                    stack.append(operator)
            elif operator == '(':
                stack.append(operator)
            elif operator == ')':
                m = len(stack)-1
                while stack[m] != '(':
                    a = stack.pop()
                    tmp_tab.append(a)
                    m-=1
                stack.pop()
            else:
                tmp_tab.append(x[i])
        while 1:
            try:
                a = stack.pop()
                tmp_tab.append(a)
            except:
                converted_tab.append(tmp_tab)
                break
    return converted_tab

def calculate_ONP(tab):
    num = 0
    for x in tab:
        stack = []
        for i in x:
            if i == '*' or i == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '*':
                    stack.append(a*b)
                else:
                    stack.append(a+b)
            else:
                stack.append(i)
        num += stack[0]
    return num

tab = reader()

#first
print('first =', calculate_ONP(convert_to_ONP_first(tab)))

#second
print('second =', calculate_ONP(convert_to_ONP_second(tab)))
