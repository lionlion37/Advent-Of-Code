######################################################
# Advent of Code 2021, Day seventeen: "Trick Shot"   #
# https://adventofcode.com/2021/day/17               #
######################################################
    
import os
import numpy as np
import re


# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day17.txt'), 'r') as f:
    entries = f.readlines()
    pattern = "target area: x=(\d*)..(\d*), y=-(\d*)..-(\d*)\n"
    result = re.search(pattern, entries[0])
    min_x = int(result.group(1))
    max_x = int(result.group(2))
    min_y = -1 * int(result.group(3))
    max_y = -1 * int(result.group(4))


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def shoot(max_x, min_x, max_y, min_y):

    possible_v = []
    for v1 in range(150):
        for v2 in range(-200, 200):
            current_v1, current_v2 = v1, v2
            current_x, current_y, max_current_y = 0, 0, 0

            for _ in range(400):
                current_x += current_v1
                current_y += current_v2
                current_v2 -= 1
                if current_v1 > 0:
                    current_v1 -= 1
                elif current_v1 < 0:
                    current_v1 += 1

                if current_y > max_current_y:
                    max_current_y = current_y

                if min_x <= current_x <= max_x and min_y <= current_y <= max_y:
                    possible_v.append([max_current_y, v1, v2])
                    break

    possible_v = np.array(possible_v)
    best_v = possible_v[np.argmax(possible_v[:, 0])][0]
    return best_v, len(possible_v)


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {shoot(max_x, min_x, max_y, min_y)[0]}')
print(f'Solution part 2: {shoot(max_x, min_x, max_y, min_y)[1]}')
