#################################################
# Advent of Code 2021, Day one: "Sonar Sweep"   #
# https://adventofcode.com/2021/day/1           #
#################################################
    
import os

# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day1.txt'), 'r') as f:
    entries = f.readlines()
    entries = [int(entry) for entry in entries]
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list):
    n_increases = 0
    current_entry = entry_list[0]

    for entry in entry_list[1:]:
        entry = entry
        if entry > current_entry:
            n_increases += 1

        current_entry = entry

    return n_increases


def part2(entry_list):
    n_increases = 0
    current_entry = entry_list[0]

    sum_list = []
    length = len(entry_list)

    for n in range(length):
        if n + 2 >= length:
            break

        sum_list.append(entry_list[n] + entry_list[n+1] + entry_list[n+2])

    current_s = sum_list[0]
    for s in sum_list:
        if s > current_s:
            n_increases += 1

        current_s = s

    return n_increases

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
