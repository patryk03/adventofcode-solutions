import re
def reader():
    with open ('data19.txt') as input_file:
        rules, messages = input_file.read().split('\n\n')
        rules = [x.split(': ') for x in rules.splitlines()]
        rules = {x: i for x, i in rules}
        messages = messages.splitlines()
    return rules, messages


def re_compiler(to_find, all_rules):
    sent = ''
    rule = all_rules[to_find]

    # if to_find == '8':
    #     to_add = re_compiler('42', all_rules)
    #     sent += '('
    #     sent += to_add
    #     for x in range(3):
    #         sent+='|'
    #         to_add += to_add
    #         sent += to_add
    #     sent+=')'
    #     return sent

    # elif to_find == '11':
    #     sent+='('
    #     to_add =re_compiler('42', all_rules)
    #     second_to_add = re_compiler('31', all_rules)
    #     sent += to_add
    #     sent+= second_to_add
    #     for x in range(3):
    #         sent+='|'
    #         to_add += to_add
    #         second_to_add += second_to_add
    #         sent+=to_add
    #         sent+=second_to_add
    #     sent+=')'
    #     return sent

    if '|' in rule:
        if to_find != '8' and to_find != '11':
            rule = rule.split(' ')
        sent += '('
        for x in rule:
            if x != '|':
                to_add = re_compiler(x, all_rules)
                sent += to_add
            else:
                sent += '|'
        sent += ')'
    elif '"' in rule:
        sent += rule.replace('"', '')
    else:
        rule = rule.split(' ')
        for x in rule:
            to_add = re_compiler(x, all_rules)
            sent += to_add
    if to_find == '8':
        sent = '('+sent+')+'
    return sent

def second_re_matcher(rules,tocheck):
    re_sent = ''
    for x in tocheck:
        re_sent += re_compiler(x, rules)
    return re_sent
    

rules, messages = reader()
rules['11'] = ['42','31','|','42','42','31','31','|','42','42','42','31','31','31','|','42','42','42','42','31','31','31','31']
a = second_re_matcher(rules, ['0'])
a = re.compile('^'+a+'$')
num= 0
for x in messages:
    if a.match(x):
        num+=1
print(num)
