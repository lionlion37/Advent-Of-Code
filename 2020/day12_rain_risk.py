##################################################
# Advent of Code 2020, Day Twelve: "Rain Risk"   #
# https://adventofcode.com/2020/day/12           #
##################################################

import os
import numpy as np
from day12_utils import spin_vector

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
with open(os.path.join('inputs', 'day12.txt'), 'r') as f:
    entry_list = f.readlines()

test_entry = ['F10\n', 'N3\n', 'F7\n', 'R90\n', 'F11\n']

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entries):
    """
    Starts at position (0, 0) and executes the given instructions in the entries list.
    :param entries: list of instructions of form "ActionValue"
    :return: the final position
    """
    direction = np.array([1, 0])
    position = np.array([0, 0])
    moves = {'N': np.array([0, 1]), 'S': np.array([0, -1]), 'E': np.array([1, 0]), 'W': np.array([-1, 0]),
             'F': direction}

    for instruction in entries:

        action = instruction[0]
        value = int(instruction[1:-1])

        if action in ['N', 'S', 'E', 'W', 'F']:
            position += moves[action] * value
        elif action in ['L', 'R']:
            direction = spin_vector(direction, value, action)
            moves['F'] = direction

    return position


def part2(entries):
    """
    Works like part1, but with slightly different interpretations of the instructions.
    :param entries: list of instructions of form "ActionValue"
    :return: the final position
    """
    waypoint = np.array([10, 1], dtype=float)
    position = np.array([0, 0], dtype=float)
    moves = {'N': np.array([0, 1]), 'S': np.array([0, -1]), 'E': np.array([1, 0]), 'W': np.array([-1, 0])}

    for instruction in entries:

        action = instruction[0]
        value = float(instruction[1:-1])

        if action in ['N', 'S', 'E', 'W']:
            waypoint += moves[action] * value
        elif action == 'F':
            position += waypoint * value
        elif action in ['L', 'R']:
            waypoint = spin_vector(waypoint, value, action)

    return position


# Solutions ------------------------------------------------------------------------------------------------------------

final_position_1 = part1(test_entry)
print(f'Solution part 1: {abs(final_position_1[0]) + abs(final_position_1[1])}')

final_position_2 = part2(entry_list)
print(f'Solution part 2: {abs(final_position_2[0]) + abs(final_position_2[1])}')
