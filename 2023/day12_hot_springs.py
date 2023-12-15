####################################################
# Advent of Code 2023, Day twelve: "hot springs"   #
# https://adventofcode.com/2023/day/12             #
####################################################
import functools
import os
import re

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'day12.txt'), 'r') as f:
    entries = f.readlines()
    input_plan = []
    for line in entries:
        form1, form2 = line.strip().split()
        form2 = form2.split(',')
        input_plan.append(tuple([form1, tuple(form2)]))

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------

pattern = r'(#+)'


def sub_question(string):
    unknown_id = string.index('?')
    new_f1_1, new_f1_2 = list(string), list(string)
    new_f1_1[unknown_id] = '#'
    new_f1_2[unknown_id] = '.'
    return ''.join(new_f1_1), ''.join(new_f1_2)


@functools.lru_cache(maxsize=128)  # memoization
def check_if_valid(line):
    f1, f2 = line

    if (len(f2) == 0 and f1 != '' and '#' in f1) or (len(f2) > 0 and f1 == ''):
        return 0
    elif (len(f2) == 0 and f1 == '') or (len(f2) == 0 and set(f1) == {'?'}):  # valid
        return 1

    elif f1[0] == '.':
        return check_if_valid(tuple([f1[1:], f2]))

    elif f1[0] == '?':
        f1_1, f1_2 = sub_question(f1)
        return check_if_valid(tuple([f1_1, f2])) + check_if_valid(tuple([f1_2, f2]))

    elif f1[0] == '#':
        seg_len = len(re.search(pattern, f1).group())
        first_seg = f1.split('.')[0]
        if seg_len == int(f2[0]):
            if f2[0] == '1' and f1.ljust(2)[1] == '?':
                return check_if_valid(tuple(['#.' + f1[2:], f2]))
            elif f1.ljust(seg_len + 1)[seg_len] == '?':
                return check_if_valid(tuple(['.' + f1[seg_len + 1:], f2[1:]]))
            else:
                return check_if_valid(tuple([f1[seg_len:], f2[1:]]))
        elif seg_len > int(f2[0]):
            return 0
        elif '?' in first_seg:
            f1_1, f1_2 = sub_question(f1)
            return check_if_valid(tuple([f1_1, f2])) + check_if_valid(tuple([f1_2, f2]))
        else:
            return 0


def part1(plan):
    result = 0
    for l in plan:
        result += check_if_valid(l)
    return result


def part2(plan):
    result = 0
    for l in plan:
        l1 = (l[0] + '?') * 5
        l2 = l[1] * 5
        result += check_if_valid(tuple([l1[:-1], tuple(l2)]))
    return result


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(input_plan)}')
print(f'Solution part 2: {part2(input_plan)}')
