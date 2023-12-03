###############################################################
# Advent of Code 2021, Day seven: "The Treachery of Whales"   #
# https://adventofcode.com/2021/day/7                         #
###############################################################
    
import os
import numpy as np
import math
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day7.txt'), 'r') as f:
    entries = f.readlines()
    entries = np.array(entries[0][:-1].split(','), dtype=int)

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list):
    return np.sum(np.abs(entry_list - np.median(entry_list)))
    
    
def part2(entry_list):
    optimal = math.ceil(math.floor(np.mean(entry_list)) - 1/2)
    result = 0
    for crab in entry_list:
        result += fuel(crab, optimal)

    return result


def fuel(x, k):
    return 1/2 * (np.power((x-k), 2) + np.abs(x - k))

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
