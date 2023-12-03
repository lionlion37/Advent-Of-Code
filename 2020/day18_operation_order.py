##########################################################
# Advent of Code 2020, Day Eighteen: "Operation Order"   #
# https://adventofcode.com/2020/day/18                   #
##########################################################
    
import os
import re
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day18.txt'), 'r') as f:
    entry_list = f.readlines()

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def operate(v1, v2, operation):
    if operation == '+':
        return v1 + v2
    elif operation == '-':
        return v1 - v2
    elif operation == '*':
        return v1 * v2


def part1(entries):
    results = []

    for equation in entries:
        done = False
        while not done:
            for n, s in enumerate(equation):
                if s == '(' and equation[n+1] == '(':
                    equation = equation[:n+1] + '0 + ' + equation[n+1:]
                    break
            else:
                done = True

        parantheses = False
        start = False
        jump = False
        if equation[0] != '(':
            current_value = int(equation[0])
        else:
            start = True

        for n, el in enumerate(equation):
            if el == '\n':
                continue
            if el == ')' and jump:
                jump = False
                continue

            if el == ' ' or jump:
                continue

            if not parantheses:
                if el in ['+', '*', '-']:
                    operation = el
                    continue
                elif el == '(':
                    sub_value = int(equation[n+1])
                    parantheses = True
                    continue
                elif n != 0 and el != ')':
                    current_value = operate(current_value, int(el), operation)

            else:
                if el in ['+', '*', '-']:
                    sub_operation = el
                    continue
                elif el == ')':
                    if start:
                        current_value = sub_value
                    else:
                        current_value = operate(current_value, sub_value, operation)
                    parantheses = False
                    continue
                elif el == '(':
                    pattern = '\(([ \d\+\-\*(]*)\)'
                    m = re.match(pattern, equation[n:])
                    sub_value = operate(sub_value, part1([m.group(1)])[0], sub_operation)
                    jump = True
                elif equation[n-1] != '(':
                    sub_value = operate(sub_value, int(el), sub_operation)

        results.append(current_value)

    return results

    
# Solutions ------------------------------------------------------------------------------------------------------------

test = ['2 * 3 + (4 * 5)', '5 + (8 * 3 + 9 + 3 * 4 * 3)', '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
r = part1(entry_list)
result = 0
for e in r:
    result += e

print(result)
