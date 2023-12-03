##################################################
# Advent of Code 2022, Day nine: "Rope Bridge"   #
# https://adventofcode.com/2022/day/9            #
##################################################

import os
import re

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'test9.txt'), 'r') as f:
    entries = f.readlines()


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(instructions):
    pattern = '(R|L|U|D) (\d+)\n'
    position_h, position_t = [0, 0], [0, 0]
    visited = set()

    for instruction in instructions:
        result = re.search(pattern, instruction)
        direction, n_steps = result.group(1), int(result.group(2))
        if direction == 'R':
            for n in range(n_steps):
                position_h[0] += 1
                position_t = move_t(position_h, position_t, direction)[0]
                visited.add(tuple(position_t))
        elif direction == 'L':
            for n in range(n_steps):
                position_h[0] -= 1
                position_t = move_t(position_h, position_t, direction)[0]
                visited.add(tuple(position_t))
        elif direction == 'U':
            for n in range(n_steps):
                position_h[1] += 1
                position_t = move_t(position_h, position_t, direction)[0]
                visited.add(tuple(position_t))
        elif direction == 'D':
            for n in range(n_steps):
                position_h[1] -= 1
                position_t = move_t(position_h, position_t, direction)[0]
                visited.add(tuple(position_t))

    return len(visited)


def move_t(position_h, position_t, instruction):

    instruction_math = {'R': [-1, 0], 'L': [1, 0], 'U': [0, -1], 'D': [0, 1],
                        'UR': [1, 0], 'UL': [-1, 0], 'DR': [0, -1], 'DL': [0, 1]}
    move_dir = instruction
    if not ((position_t[0] in [position_h[0], position_h[0] + 1, position_h[0] - 1]) and
            (position_t[1] in [position_h[1], position_h[1] + 1, position_h[1] - 1])):

        move = [position_h[0] - position_t[0] + instruction_math[instruction][0], position_h[1] -
                position_t[1] + instruction_math[instruction][1]]
        position_t[0], position_t[1] = position_t[0] + move[0], position_t[1] + move[1]

        if move == [1, 1]:
            move_dir = 'UR'
        elif move == [-1, 1]:
            move_dir = 'UL'
        elif move == [-1, -1]:
            move_dir = 'DL'
        elif move == [1, -1]:
            move_dir = 'DR'
        elif move == [1, 0]:
            move_dir = 'R'
        elif move == [-1, 0]:
            move_dir = 'L'
        elif move == [0, 1]:
            move_dir = 'U'
        elif move == [0, -1]:
            move_dir = 'D'

    return position_t, move_dir


def update_tails(h, t1, t2, t3, t4, t5, t6, t7, t8, t9, instruction):
    current_head = h
    current_dir = instruction
    tails = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
    for n, current_tail in enumerate(tails):
        tails[n], current_dir = move_t(current_head, current_tail, current_dir)
        current_head = tails[n]

    return tails[0], tails[1], tails[2], tails[3], tails[4], tails[5], tails[6], tails[7], tails[8]


def part2(instructions):
    pattern = '(R|L|U|D) (\d+)\n'
    h, t1, t2, t3, t4, t5, t6, t7, t8, t9 = [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], \
                                            [0, 0]
    visited = set()

    for instruction in instructions:
        result = re.search(pattern, instruction)
        direction, n_steps = result.group(1), int(result.group(2))
        if direction == 'R':
            for n in range(n_steps):
                h[0] += 1
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = update_tails(h, t1, t2, t3, t4, t5, t6, t7, t8, t9, direction)
                visited.add(tuple(t9))
        elif direction == 'L':
            for n in range(n_steps):
                h[0] -= 1
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = update_tails(h, t1, t2, t3, t4, t5, t6, t7, t8, t9, direction)
                visited.add(tuple(t9))
        elif direction == 'U':
            for n in range(n_steps):
                h[1] += 1
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = update_tails(h, t1, t2, t3, t4, t5, t6, t7, t8, t9, direction)
                visited.add(tuple(t9))
        elif direction == 'D':
            for n in range(n_steps):
                h[1] -= 1
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = update_tails(h, t1, t2, t3, t4, t5, t6, t7, t8, t9, direction)
                visited.add(tuple(t9))

    return len(visited)


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
