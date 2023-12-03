###############################################################
# Advent of Code 2022, Day three: "Rucksack Reorganization"   #
# https://adventofcode.com/2022/day/3                         #
###############################################################
    
import os
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day3.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list):
    score = 0
    for rucksack in entry_list:
        n = len(rucksack) - 1
        comp1, comp2 = set(rucksack[:int((n/2))]), set(rucksack[int((n/2)):-1])
        item = comp1.intersection(comp2).pop()
        if item.isupper():
            score += (ord(item) - 38)
        else:
            score += (ord(item) - 96)

    return score
    
    
def part2(entry_list):
    score = 0
    for n in range(0, len(entry_list), 3):
        rucksack1, rucksack2, rucksack3 = set(entry_list[n][:-1]), set(entry_list[n+1][:-1]), set(entry_list[n+2][:-1])
        badge = rucksack1.intersection(rucksack2).intersection(rucksack3).pop()
        if badge.isupper():
            score += (ord(badge) - 38)
        else:
            score += (ord(badge) - 96)
    return score

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
