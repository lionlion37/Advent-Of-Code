###################################################
# Advent of Code 2020, Day One: "Report Repair"   #
# https://adventofcode.com/2020/day/1             #
###################################################

import os

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def sum_finder(entries, given_sum):
    """
    Find two entries that sum up to a given number and return their product.
    :param entries: list of entries
    :param given_sum: number that two entries should sum up to
    :return: result: product of two entries that sum up to a given number, done: boolean that shows if two entries
    could be found
    """
    done = False
    result = 0
    for n, el1 in enumerate(entries):
        if done:
            break
        for el2 in entries[n:]:
            sum = el1 + el2
            if sum == given_sum:
                result = el1 * el2
                done = True
                break

    return result, done


def part2(entries):
    """
    Find three entries that sum up to 2020 and return their product.
    :param entries: list of entries
    :return: product of three entries that sum up to 2020
    """
    done = False
    result = 0
    for n, el1 in enumerate(entries):
        if done:
            break
        for m, el2 in enumerate(entries[n:]):
            if done:
                break
            for el3 in entries[m:]:
                sum = el1 + el2 + el3
                if sum == 2020:
                    result = el1 * el2 * el3
                    break

    return result


if __name__ == '__main__':

    # get input --------------------------------------------------------------------------------------------------------

    # import puzzle input
    with open(os.path.join('inputs', 'day1.txt'), 'r') as f:
        entry_list = f.readlines()
        entry_list = [int(el) for el in entry_list if el != '\n']

    # Solutions --------------------------------------------------------------------------------------------------------

    print(f'Solution part 1: {sum_finder(entry_list, 2020)[0]}')
    print(f'Solution part 2: {part2(entry_list)}')
