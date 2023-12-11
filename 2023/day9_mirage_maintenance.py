#########################################################
# Advent of Code 2023, Day nine: "mirage maintenance"   #
# https://adventofcode.com/2023/day/9                   #
#########################################################
    
import os
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day9.txt'), 'r') as f:
    entries = f.readlines()
entries = np.array([np.array(entry.split(), dtype=int) for entry in entries])
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def process_sequence(seq, reverse=False):
    last_elements = []
    if reverse:
        current_seq = seq[::-1]
    else:
        current_seq = seq
    while set(current_seq) != {0}:
        last_elements.append(current_seq[-1])
        current_seq = current_seq[1:] - current_seq[:-1]
    return np.sum(last_elements)


def solve(entry_list, reverse=False):
    result = 0
    for seq in entry_list:
        result += process_sequence(seq, reverse)

    return result


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {solve(entries)}')
print(f'Solution part 2: {solve(entries, reverse=True)}')