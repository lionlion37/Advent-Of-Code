#######################################################
# Advent of Code 2020, Day Eleven: "Seating System"   #
# https://adventofcode.com/2020/day/11                #
#######################################################

import os
import numpy as np
from day11_utils import simulate_seats

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
entry_list = []
with open(os.path.join('inputs', 'day11.txt'), 'r') as f:
    for line in f.readlines():
        entry_list.append([0 if s == 'L' else -1 for s in line[:-1]])
entry_list = np.array(entry_list)

test_entry = []
test_input = ['L.LL.LL.LL',
              'LLLLLLL.LL',
              'L.L.L..L..',
              'LLLL.LL.LL',
              'L.LL.LL.LL',
              'L.LLLLL.LL',
              '..L.L.....',
              'LLLLLLLLLL',
              'L.LLLLLL.L',
              'L.LLLLL.LL']
for line in test_input:
    test_entry.append([0 if s == 'L' else -1 for s in line])
test_entry = np.array(test_entry)

# function for part 1 and part 2 of the puzzle -------------------------------------------------------------------------


def part(entries, part):
    """
    Fills the given seats either after the rules of part 1 or part 2. To select a specific set of rules, set the
    parameter -part- to either 1 (rules of part 1) or 2 (rules of part 2).
    :param entries: current state of the waiting area
    :param part: select set of rules to apply by either setting this to 1 or 2
    :return: current_state: final state fo waiting area where nothing will change anymore, n: number of occupied seats
    """
    i = 1
    current_stage = simulate_seats(entries, part=part)
    while True:
        print(i)
        next_stage = simulate_seats(current_stage, part=part)
        if np.all(current_stage == next_stage):
            break
        else:
            current_stage = next_stage
            i += 1
    n = np.count_nonzero(current_stage == 1)
    return current_stage, n


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part(entry_list, part=1)[1]}')
print(f'Solution part 2: {part(entry_list, part=2)[1]}')
