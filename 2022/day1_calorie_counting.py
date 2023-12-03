######################################################
# Advent of Code 2022, Day one: "Calorie Counting"   #
# https://adventofcode.com/2022/day/1                #
######################################################
    
import os
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day1.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list):
    return max([sum(map(int, elve.split('\n'))) for elve in ''.join(entries).split('\n\n')])
    
    
def part2(entry_list):
    return sum(sorted([sum(map(int, elve.split('\n'))) for elve in ''.join(entries).split('\n\n')], reverse=True)[:3])

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
