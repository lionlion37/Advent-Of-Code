############################################################
# Advent of Code 2022, Day seven: "NoSpaceLeft OnDevice"   #
# https://adventofcode.com/2022/day/7                      #
############################################################
    
import os
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day7.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def solution(entry_list):
    stack, sizes = [], []
    total_size = 0

    for line in entry_list:
        if line == '$ cd ..\n':
            size = stack.pop()
            sizes.append(size)
            stack[-1] += size

        elif line.startswith('$ cd'):
            stack.append(0)

        elif line[0].isdigit():
            stack[-1] += int(line.split()[0])
            total_size += int(line.split()[0])

    sizes = np.array(sizes)

    unused_space = 70000000 - total_size
    space_missing = 30000000 - unused_space
    to_delete = np.min(sizes[sizes >= space_missing])

    return np.sum(sizes[sizes <= 100000]), to_delete


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {solution(entries)[0]}')
print(f'Solution part 2: {solution(entries)[1]}')
