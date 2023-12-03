####################################################
# Advent of Code 2022, Day six: "Tuning Trouble"   #
# https://adventofcode.com/2022/day/6              #
####################################################
    
import os
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day6.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def solution(entry_list, len_message):
    buffer = entry_list[0][:-1]

    for n in range(len(buffer)):
        possible_marker = buffer[n:(n+len_message)]
        if len(set(possible_marker)) == len_message:
            return n+len_message


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {solution(entries, len_message=4)}')
print(f'Solution part 2: {solution(entries, len_message=14)}')
