###################################################
# Advent of Code 2021, Day six: "Lanternfish"   #
# https://adventofcode.com/2021/day/6             #
###################################################
    
import os
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day6.txt'), 'r') as f:
    entries = f.readlines()
    entries = np.array(entries[0][:-1].split(','), dtype=int)

# entries = np.array([3,4,3,1,2])

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def reproduce(fish, days):
    ages = np.array([0] * 9)
    for n in fish:
        ages[n] += 1

    for day in range(days):
        ages = np.roll(ages, -1)
        ages[6] += ages[8]

    return np.sum(ages)


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {reproduce(entries, 80)}')
print(f'Solution part 2: {reproduce(entries, 256)}')
