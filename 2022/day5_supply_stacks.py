####################################################
# Advent of Code 2022, Day five: "Supply Stacks"   #
# https://adventofcode.com/2022/day/5              #
####################################################
    
import os
import numpy as np
import re
import time

# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day5.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------

def part1(entry_list):

    # Read input
    stacks = list()
    n_stacks = len(entry_list[0]) / 4
    pattern = '(\w)|(    )'

    for n, line in enumerate(entry_list):
        if re.search('\d', line):
            break
        else:
            res = re.findall(pattern, line)
            stacks.insert(0, [s[0] for s in res])

    stacks = np.transpose(np.array(stacks)).tolist()
    for i, stack in enumerate(stacks):
        current_stack = ''.join(stack).strip()
        stacks[i] = list(current_stack)

    pattern = 'move (\d+) from (\d+) to (\d+)'

    for command in entry_list[(n+2):]:
        res = re.search(pattern, command)
        n_crates, start, end = int(res.group(1)), int(res.group(2)) - 1, int(res.group(3)) - 1
        for t in range(n_crates):
            curr_crate = stacks[start].pop()
            stacks[end].append(curr_crate)

            # for s in stacks:
            #     print(s)
            # time.sleep(1)
            # os.system('clear')

    solution = ''.join([stack[-1] for stack in stacks])

    return solution
    
def part2(entry_list):

    # Read input
    stacks = list()
    n_stacks = len(entry_list[0]) / 4
    pattern = '(\w)|(    )'

    for n, line in enumerate(entry_list):
        if re.search('\d', line):
            break
        else:
            res = re.findall(pattern, line)
            stacks.insert(0, [s[0] for s in res])

    stacks = np.transpose(np.array(stacks)).tolist()
    for i, stack in enumerate(stacks):
        current_stack = ''.join(stack).strip()
        stacks[i] = list(current_stack)

    pattern = 'move (\d+) from (\d+) to (\d+)'

    for command in entry_list[(n+2):]:
        res = re.search(pattern, command)
        n_crates, start, end = int(res.group(1)), int(res.group(2)) - 1, int(res.group(3)) - 1

        curr_stack = stacks[start]
        curr_crates = curr_stack[len(curr_stack)-n_crates:]
        stacks[start] = curr_stack[:len(curr_stack)-n_crates]
        for c in curr_crates:
            stacks[end].append(c)

            """for s in stacks:
                print(s)
            time.sleep(1)
            os.system('clear')"""

    solution = ''.join([stack[-1] for stack in stacks])

    return solution

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
