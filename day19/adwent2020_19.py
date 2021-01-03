import copy
def reader():
    with open ('data19.txt') as input_file:
        tab = input_file.read().split('\n\n')
        letters = dict()
        first_rules = tab[0].split('\n')
        rules = dict()
        first_rule = []
        for x in first_rules:
            num, rest = x.split(': ')
            if num == '0':
                first_rule = rest.split(' ')
            elif '"' not in rest:
                rest = [x.split(' ') for x in rest.split(' | ')]
                rules[int(num)] = rest
            else:
                letters[int(num)] = rest.replace('"', '')
        messages = tab[1].splitlines()
    return rules, letters, messages, first_rule

def rules_loop(rules, letters, toCheck):
    part_to_return = [[]]
    for x in toCheck:
        toAdd = []
        for i in x:
            if int(i) in rules:
                toAdd = rules_loop(rules, letters, rules[int(i)])
                part_to_return[-1].append(toAdd)
            else:
                part_to_return[-1].extend(letters[int(i)])
        part_to_return.append([])
    return part_to_return[:-1]

def valid_message_creator(rules, letters, messages, first_rule):
    valid_letters_to_add = []
    valid_rules = []
    for x in first_rule:
        if int(x) not in rules:
            valid_letters_to_add.append(letters[int(x)])
        else:
            rule_tab = rules_loop(rules, letters, rules[int(x)])
            later_rule_tab = []
            for f in rule_tab:
                for i in f[0]:
                    for m in f[1]:
                        later_rule_tab.append(copy.copy(i))
                        later_rule_tab[-1].extend(m)
            for f in later_rule_tab:
                for m in valid_letters_to_add:
                    f.insert(0, m)
            later_rule_tab.append(len(valid_letters_to_add)-1)
            valid_rules.append(later_rule_tab)
    for x in valid_rules:
        letters_range = x.pop()+1
        for i in x:
            for m in range(letters_range, len(valid_letters_to_add)):
                i.append(valid_letters_to_add[m])
    return valid_messages_counter(valid_rules, [list(x) for x in messages])

def valid_messages_counter(valid_rules, messages):
    num = 0
    for i in messages:
        for x in valid_rules:
            if i in x:
                num +=1
    return num



rules, letters, messages, first_rule = reader()
print(valid_message_creator(rules, letters, messages, first_rule))