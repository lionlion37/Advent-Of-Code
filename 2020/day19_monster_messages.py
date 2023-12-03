###########################################################
# Advent of Code 2020, Day Nineteen: "Monster Messages"   #
# https://adventofcode.com/2020/day/19                    #
###########################################################
    
import os
import re
from itertools import permutations

# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day19.txt'), 'r') as f:
    entry_rules = [''] * 134
    signals = []
    for n, line in enumerate(f.readlines()):
        if ':' in line:
            entry_rules[int(line[:-1].split(':')[0])] = line[:-1]
        elif line != '\n':
            signals.append(line[:-1])

test_1 = '''0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"'''
test_2 = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
'''
test_1 = test_1.split('\n')
test_2 = test_2.split('\n')

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def get_rules(rules, rule):
    if '"' in rules[int(rule)]:
        return re.search('\"([ab])\"', rules[int(rule)]).group(1)
        # return 0 if re.search('\"([ab])\"', rules[int(rule)]).group(1) == 'a' else 1
    else:

        if '|' in rules[int(rule)]:
            references = re.search('\d+: ([\d |]+)', rules[int(rule)]).group(1)
            reference_1, reference_2 = references.split('|')
            reference_1 = reference_1.strip().split(' ')
            reference_2 = reference_2.strip().split(' ')
            output_1 = []
            output_2 = []
            for r1, r2 in zip(reference_1, reference_2):
                output_1.append({'p1': get_rules(rules, r1)})
                output_2.append({'p2': get_rules(rules, r2)})
            return [output_1, output_2]

        else:
            references = re.search('\d+: ([\d |]+)', rules[int(rule)]).group(1).split(' ')
            output = []
            for r in references:
                output.append(get_rules(rules, r))
            return output


def sum_strings(rules):
    if (type(rules) == list and not any(isinstance(r, list) for r in rules)) or (type(rules) == str):
        return ''.join(rules) if len(rules) > 1 else rules
    else:
        output = []
        for nest in rules:
            output.append(sum_strings(nest))
        return output


def generate_pos(rules):
    list_to_permute = list(range(rules))


# Solutions ------------------------------------------------------------------------------------------------------------

r = get_rules(test_2, 0)

print(r)
