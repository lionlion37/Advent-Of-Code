#####################################################
# Advent of Code 2020, Day Nine: "Encoding Error"   #
# https://adventofcode.com/2020/day/9               #
#####################################################

import os
from day1_report_repair import sum_finder

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
entry_list = []
with open(os.path.join('inputs', 'day9.txt'), 'r') as f:
    for l in f.readlines():
        entry_list.append(int(l))

test_entry = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entries, len_preamble):
    """
    Checks if all entries in the given list are valid according to the rules stated on the AoC website. Returns the
    first invalid entry.
    :param entries: list of numbers
    :param len_preamble: length of preamble to validate entry
    :return: first invalid entry
    """
    for t, number in enumerate(entries[len_preamble:]):
        pool = entries[t:t+len_preamble]
        _, valid = sum_finder(pool, number)
        if not valid:
            return number
    else:
        print('All entries are valid!')
        return None


def part2(entries, len_preamble):
    """
    Searches for a contiguous set of at least two numbers that sum up to the first invalid number in the entry list.
    :param entries: list of numbers
    :param len_preamble: length of preamble to validate entry
    :return: smallest and largest number in contiguous set if one was found, otherwise None
    """
    invalid_number = part1(entries, len_preamble)
    for t, lower in enumerate(entries):
        for s, upper in enumerate(entries[t+1:]):
            sum = 0
            for q in range(t, s+t+1):
                sum += entries[q]
            if sum == invalid_number:
                set = entries[t:t+s+1]
                return min(set), max(set)
    else:
        print('No set found!')
        return None


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part1(entry_list, 25)}')
print(f'Solution part 2: {part2(entry_list, 25)[0] + part2(entry_list, 25)[1]}')
