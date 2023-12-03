####################################################
# Advent of Code 2023, Day two: "Cube Conundrum"   #
# https://adventofcode.com/2023/day/2              #
####################################################
    
import os
import re
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day2.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list, n_red, n_green, n_blue):

    pattern = 'Game (\d+): (.*)'
    result_1 = 0
    result_2 = 0

    for game in entry_list:
        search_result = re.search(pattern, game)
        n_group = search_result.group(1)
        game = search_result.group(2)

        for color, color_id in (('blue', '0'), ('red', '1'), ('green', '2')):
            game = game.replace(color, color_id)

        subsets_counts = []
        for subset in game.split(';'):
            current_counts = np.zeros(3)
            for cube in subset.split(','):
                cube = cube.strip().split(' ')
                current_counts[int(cube[1])] += int(cube[0])
            subsets_counts.append(current_counts)
        subsets_counts = np.array(subsets_counts)

        if np.sum(subsets_counts > np.array([n_blue, n_red, n_green])) == 0:
            result_1 += int(n_group)

        power = np.prod(np.max(subsets_counts.T, axis=1))
        result_2 += int(power)

    return result_1, result_2


# Solutions ------------------------------------------------------------------------------------------------------------

results = part1(entries, 12, 13, 14)
print(f'Solution part 1: {results[0]}')
print(f'Solution part 2: {results[1]}')
