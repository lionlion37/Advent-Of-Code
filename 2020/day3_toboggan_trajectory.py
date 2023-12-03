###########################################################
# Advent of Code 2020, Day Three: "Toboggan Trajectory"   #
# https://adventofcode.com/2020/day/2                     #
###########################################################

import os

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
with open(os.path.join('inputs', 'day3.txt'), 'r') as f:
    entry_list = f.readlines()

test_entry = ['..##.......\n',
              '#...#...#..\n',
              '.#....#..#.\n',
              '..#.#...#.#\n',
              '.#...##..#.\n',
              '..#.##.....\n',
              '.#.#.#....#\n',
              '.#........#\n',
              '#.##...#...\n',
              '#...##....#\n',
              '.#..#...#.#\n']


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def toboggan(entries, right, down):
    """
    Takes a map of trees as an input and calculates how many trees will be hit if the map is driven through with a
    costant slope of *right* steps to the right and *down* steps down. If the right end of the map is reached, the map
    will be duplicated.
    :param entries: map of trees as a list with rows as list elements
    :param right: steps right per slope
    :param down: steps down per slope
    :return: number of trees hit until the last row is reached
    """
    len_lines = len(entries[0]) - 1
    n_trees = 0
    n_overflow = 0
    n = 0
    current_row = 0
    while True:
        current_row = down * n
        if current_row >= len(entries):
            break
        line = entries[current_row]
        line = line[:(len(line) - 1)]
        if current_row == 0:
            n += 1
            continue
        if (n * right) > (len_lines * (n_overflow + 1) - 1):
            n_overflow += 1
        current_id = (n * right) - len_lines * n_overflow
        if line[current_id] == '#':
            n_trees += 1
        n += 1

    return n_trees


def part2(entries):
    return toboggan(entry_list, 1, 1) * toboggan(entry_list, 3, 1) * toboggan(entry_list, 5, 1) * \
           toboggan(entry_list, 7, 1) * toboggan(entry_list, 1, 2)


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {toboggan(entry_list, 3, 1)}')
print(f'Solution part 2: {part2(entry_list)}')
