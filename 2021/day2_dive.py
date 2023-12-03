###########################################
# Advent of Code 2021, Day two: "Dive!"   #
# https://adventofcode.com/2021/day/2     #
###########################################
    
import os
import re

# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day2.txt'), 'r') as f:
    entries = f.readlines()

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def move(entry_list, commands: dict):

    aim = sum([el[2] == 1 for el in commands.values()])
    position = [0, 0, int(not aim)]

    for instruction in entry_list:
        result = re.search("(\D+) (\d+)\n", instruction)
        command, units = commands[result.group(1)], int(result.group(2))
        position[command[0]] += units * command[1]
        position[1] += units * position[2] * command[2]

    return position[0] * position[1]


# Solutions ------------------------------------------------------------------------------------------------------------


commands_p1 = {'forward': [0, 1, 0], 'up': [1, -1, 0], 'down': [1, 1, 0]}
commands_p2 = {'forward': [0, 1, 1], 'up': [2, -1, 0], 'down': [2, 1, 0]}

print(f'Solution part 1: {move(entries, commands_p1)}')
print(f'Solution part 2: {move(entries, commands_p2)}')
