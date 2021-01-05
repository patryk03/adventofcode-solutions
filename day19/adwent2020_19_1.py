import re
def reader():
    with open ('data19.txt') as input_file:
        rules, messages = input_file.read().split('\n\n')
        rules = [x.split(': ') for x in rules.splitlines()]
        rules = {x: i for x, i in rules}
        messages = messages.splitlines()
    return rules, messages

def re_matcher(rules, messages):
    ans = 0
    re_sent = ''
    zero = rules['0'].split(' ')
    for x in zero:
        re_sent += re_compiler(x, rules)
    compiled = re.compile(re_sent)
    for x in messages:
        if re.fullmatch(compiled, x):
            ans += 1
    return ans

def re_compiler(to_find, all_rules):
    sent = ''
    rule = all_rules[to_find]
    if '|' in rule:
        rule = rule.split(' ')
        sent += '('
        for x in rule:
            if x != '|':
                to_add = re_compiler(x, all_rules)
                sent += to_add
            else:
                sent += '|'
        sent += ')'
        return sent
    elif '"' in rule:
        sent += rule.replace('"', '')
        return sent
    else:
        rule = rule.split(' ')
        for x in rule:
            to_add = re_compiler(x, all_rules)
            sent += to_add
        return sent

def second_re_matcher(rules, messages):
    ans = 0
    re_sent = ''
    zero = rules['0'].split(' ')
    for x in zero:
        re_sent += re_compiler(x, rules)
    compiled = re.compile(re_sent)
    for x in messages:
        if re.fullmatch(compiled, x):
            ans += 1
    return ans


rules, messages = reader()
print(re_matcher(rules, messages))