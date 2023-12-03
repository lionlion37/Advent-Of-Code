###################################################
# Advent of Code 2022, Day four: "Camp Cleanup"   #
# https://adventofcode.com/2022/day/4             #
###################################################
    
import os
import re

# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day4.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list):
    n_contain = 0
    for pair in entry_list:
        pattern = '(\d+)-(\d+),(\d+)-(\d+)'
        result = re.search(pattern, pair)
        elve11, elve12, elve21, elve22 = int(result.group(1)), int(result.group(2)), int(result.group(3)), \
                                         int(result.group(4))
        if (elve11 <= elve21 and elve22 <= elve12) or (elve21 <= elve11 and elve12 <= elve22):
            n_contain += 1

    return n_contain
    

def part2(entry_list):
    n_contain = 0
    for pair in entry_list:
        pattern = '(\d+)-(\d+),(\d+)-(\d+)'
        result = re.search(pattern, pair)
        elve11, elve12, elve21, elve22 = int(result.group(1)), int(result.group(2)), int(result.group(3)), \
                                         int(result.group(4))
        if (elve11 <= elve21 and elve22 <= elve12) or (elve21 <= elve11 and elve12 <= elve22) or \
           (elve11 <= elve21 <= elve12 <= elve22) or \
           (elve21 <= elve11 <= elve22 <= elve12):
            n_contain += 1

    return n_contain

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
