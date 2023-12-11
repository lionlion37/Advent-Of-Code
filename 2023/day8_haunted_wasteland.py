#########################################################
# Advent of Code 2023, Day eight: "haunted wasteland"   #
# https://adventofcode.com/2023/day/8                   #
#########################################################
    
import os
import re
import numpy as np
from math import lcm
    
# get input ------------------------------------------------------------------------------------------------------------

pattern = r'(...) = \((...), (...)'
with open(os.path.join('inputs', 'day8.txt'), 'r') as f:
    entries = f.readlines()
    instructions = list(entries[0].strip())
    instructions = np.array(np.array(instructions) == 'R', dtype=int)
    steps = {}
    for s in entries[2:]:
        res = re.search(pattern, s)
        steps[res.group(1)] = [res.group(2), res.group(3)]

    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def calculate_paths(instructions, step_dict, start_node, part2=False):
    result = 0
    current_node = start_node

    if not part2:
        while current_node != 'ZZZ':
            for i in instructions:
                current_node = step_dict[current_node][i]
                result += 1
    else:
        while current_node[-1] != 'Z':
            for i in instructions:
                current_node = step_dict[current_node][i]
                result += 1

    return result
    
    
def part2(instructions, step_dict):

    current_nodes = [n for n in step_dict.keys() if n[-1] == 'A']

    path_lengths = []
    for n in current_nodes:
        path_lengths.append(calculate_paths(instructions, step_dict, n, part2=True))

    result = lcm(*path_lengths)

    return result

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {calculate_paths(instructions, steps, "AAA")}')
print(f'Solution part 2: {part2(instructions, steps)}')
