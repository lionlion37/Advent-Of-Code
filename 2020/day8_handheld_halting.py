########################################################
# Advent of Code 2020, Day Eight: "Handheld Halting"   #
# https://adventofcode.com/2020/day/8                  #
########################################################

import os
import copy

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
entry_list = []
with open(os.path.join('inputs', 'day8.txt'), 'r') as f:
    for line in f.readlines():
        l_parts = line.split(' ')
        entry_list.append([l_parts[0], int(l_parts[1]), False])

test = [['nop', 0, False], ['acc', 1, False], ['jmp', 4, False],
        ['acc', 3, False], ['jmp', -3, False], ['acc', -99, False],
        ['acc', 1, False], ['jmp', -4, False], ['acc', 6, False]]

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entries):
    """
    Checks if a set of instructions is leading to an infinite loop. If this is the case, the -accumulator- right before
    the entering of the loop is returned. If there isn't an infinite loop, the -accumulator- at the end of the "program"
    will be returned.
    :param entries: Set of instructions of form of [*operator*, *argument*, *was_already_run*]
    :return: accumulator: last accumulator after executing the instructions (see above), loop: True when the
    instructions are leading to an infinite loop, in the other case False, instruction_order: order in which the
    instructions are run
    """
    entries_copy_1 = copy.deepcopy(entries)
    accumulator = 0
    n = 0
    loop = False
    instruction_order = []
    while True:
        instruction_order.append(n)
        operation = entries_copy_1[n][0]
        argument = entries_copy_1[n][1]
        was_repeated = entries_copy_1[n][2]

        # check if instruction was already run
        if was_repeated:
            loop = True
            break
        else:
            entries_copy_1[n][2] = True

        # run instruction
        if operation == 'acc':
            accumulator += argument
            n += 1

        elif operation == 'jmp':
            n += argument

        elif operation == 'nop':
            n += 1

        if n >= len(entries):
            break

    return accumulator, loop, instruction_order


def part2(entries):
    """
    Changes a set of instructions which are leading to an infinite loop to one which can be executed till the end.
    Returns either the final accumulator or None when the set couldn't be fixed.
    :param entries: Set of instructions of form of [*operator*, *argument*, *was_already_run*]
    :return: final accumulator of fixed set or None if the set couldn't be fixed
    """
    _, loop, instruction_order = part1(entries)
    n = len(instruction_order) - 2
    while loop:
        entries_copy = copy.deepcopy(entries)

        while True:
            entry_id = instruction_order[n]
            if entries_copy[entry_id][0] == 'jmp':
                entries_copy[entry_id][0] = 'nop'
                break
            elif entries_copy[entry_id][0] == 'nop':
                entries_copy[entry_id][0] = 'jmp'
                break
            else:
                n -= 1

        accumulator, loop, _ = part1(entries_copy)

        if not loop:
            return accumulator

        n -= 1

        if n < 0:
            print('Unable to find solution!')
            return None


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part1(entry_list)[0]}')
print(f'Solution part 2: {part2(entry_list)}')
