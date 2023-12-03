##################################################
# Advent of Code 2023, Day one: "Trebuchet ?!"   #
# https://adventofcode.com/2023/day/1            #
##################################################
    
import os
import re
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day1.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list):
    result = 0
    for line in entry_list:
        l_num = re.sub("[^0-9]", "", line)
        if l_num == '':
            continue
        cal_val = l_num[0] + l_num[-1]
        result += int(cal_val)

    return result

    
def part2(entry_list):
    word_digit_pairs = [
        ('one', 'o1e'),
        ('two', 't2o'),
        ('three', 't3e'),
        ('four', 'f4r'),
        ('five', 'f5e'),
        ('six', 's6x'),
        ('seven', 's7n'),
        ('eight', 'e8t'),
        ('nine', 'n9e')
    ]

    result = 0

    for line in entries:
        for word, digit in word_digit_pairs:
            line = line.replace(word, digit)
        l_num = re.sub("[^0-9]", "", line)
        cal_val = l_num[0] + l_num[-1]
        result += int(cal_val)

    return result

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
