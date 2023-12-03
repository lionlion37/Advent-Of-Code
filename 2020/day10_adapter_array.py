###################################################
# Advent of Code 2020, Day Ten: "Adapter Array"   #
# https://adventofcode.com/2020/day/10            #
###################################################

import os
import re

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
with open(os.path.join('inputs', 'day10.txt'), 'r') as f:
    entry_list = [int(n) for n in f.readlines()]

test_entry_1 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4,
                2, 34, 10, 3]  # 19208

test_entry_2 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]  # 8

test_entry_3 = [10, 6, 4, 7, 1, 5]  # 4

test_entry_4 = [4, 11, 7, 8, 1, 6, 5]  # 7

test_entry_5 = [3, 1, 6, 2]  # 4

test_entry_6 = [17, 6, 10, 5, 13, 7, 1, 4, 12, 11, 14]  # 28

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entries):
    """
    Counts the number of differences of 3 and number of differences of 1 in a sorted list.
    :param entries: list of integers
    :return: one_jolt: number of differences of 1, three_jolt: number of differences of 3
    """
    entries = sorted(entries)
    one_jolt = 0
    three_jolt = 1
    if entries[0] == 1:
        one_jolt += 1
    elif entries[0] == 3:
        three_jolt += 1

    for n, el in enumerate(entries):

        if n == len(entries) - 1:
            break

        if entries[n + 1] - el == 1:
            one_jolt += 1

        elif entries[n + 1] - el == 3:
            three_jolt += 1

        else:
            continue

    return one_jolt, three_jolt


def part2(entries):
    """
    Between every adapter there is a difference of either 1 or 3. When there's a difference of three, the following
    adapter can only be reached only by its previous one. Therefore a sorted list of entries can be divided into groups
    of differences, particularly into the groups which can be found in the input: (1) 313, (2) 3113, (3) 1113,
    (4) 311113. There is 1 way to go through groups of type (1), 2 ways to go through groups of type (2), 4 ways to go
    through groups of type (3) and 7 ways to go through groups of type (4). Since the order of the groups can't be
    changed, there is a total of 2^(n_groups_type_2) * 4^(n_groups_type_3) * 7 ^ (n_groups_type_4). This function looks
    for the number of different groups and return the total number of possible combinations of all entries following the
    rules defined on the AoC website.
    :param entries: list of entries, int
    :return: number of possible combinations
    """
    entries = [0] + sorted(entries)
    differences = [el - entries[n] for n, el in enumerate(entries[1:])]
    d_string = '3'

    # generate string of differences with added '3' at beginning and ending as well as after every '3' to make pattern
    # recognition easier
    for el in differences:
        if el == 3:
            d_string += 2 * str(el)
        else:
            d_string += str(el)

    d_string += '3'

    pattern_two = '3113'
    pattern_three = '31113'
    pattern_four = '311113'

    x = len(re.findall(pattern_two, d_string))
    y = len(re.findall(pattern_three, d_string))
    z = len(re.findall(pattern_four, d_string))

    return pow(2, x) * pow(4, y) * pow(7, z)


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part1(entry_list)[0] * part1(entry_list)[1]}')
print(f'Solution part 2: {part2(entry_list)}')
