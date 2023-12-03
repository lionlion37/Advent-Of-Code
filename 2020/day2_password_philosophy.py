#########################################################
# Advent of Code 2020, Day Two: "Password Philosophy"   #
# https://adventofcode.com/2020/day/2                   #
#########################################################

import os
import re

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
with open(os.path.join('inputs', 'day2.txt'), 'r') as f:
    entry_list = f.readlines()

test_list = ['1-3 a: abcde\n', '1-3 b: cdefg\n', '2-9 c: ccccccccc']

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entries):
    """
    Takes a list with entries of the form "-*lower_bound*-*upper_bound* *letter*: *password*" and checks if the given
    *letter* appears between *lower_bound* and *upper_bound* times. The function returns the number of correct passwords
    in a given list.
    :param entries: list with entries of the form "-*lower_bound*-*upper_bound* *letter*: *password*"
    :return: number of valid passwords
    """
    n_correct_passwords = 0
    pattern = '(\d*)-(\d*) ([a-z]): ([a-z]*)'
    for pwd in entries:
        n_letter = 0
        match_obj = re.search(pattern, pwd)
        lw_bnd = int(match_obj.group(1))
        up_bnd = int(match_obj.group(2))
        letter = match_obj.group(3)
        password = match_obj.group(4)

        for l in password:
            if l == letter:
                n_letter += 1

        if lw_bnd <= n_letter <= up_bnd:
            n_correct_passwords += 1

    return n_correct_passwords


def part2(entries):
    """
    Takes a list with entries of the form "-*pos1*-*pos2* *letter*: *password*" and checks if the given *letter* appears
    exactly at one of the two given positions *pos1* or *pos2*. If it appears at both or at neither one, the given
    password is invalid.
    :param entries: list with entries of the form "-*pos1*-*pos2* *letter*: *password*"
    :return: number of valid passwords
    """
    n_correct_passwords = 0
    pattern = '(\d*)-(\d*) ([a-z]): ([a-z]*)'
    for pwd in entries:
        match_obj = re.search(pattern, pwd)
        lw_id = int(match_obj.group(1)) - 1
        up_id = int(match_obj.group(2)) - 1
        letter = match_obj.group(3)
        password = match_obj.group(4)
        pos1 = password[lw_id] == letter
        pos2 = password[up_id] == letter

        if (pos1 or pos2) and not (pos1 and pos2):
            n_correct_passwords += 1

    return n_correct_passwords


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part1(entry_list)}')
print(f'Solution part 2: {part2(entry_list)}')
