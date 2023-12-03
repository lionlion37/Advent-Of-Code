###########################################################
# Advent of Code 2021, Day five: "Hydrothermal Venture"   #
# https://adventofcode.com/2021/day/5                     #
###########################################################
    
import os
import re
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day5.txt'), 'r') as f:
    entries = f.readlines()


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def hydro(entry_list, diagonal):
    pattern = "(\d+),(\d+) -> (\d+),(\d+)"
    lines = []
    max_x = 0
    max_y = 0

    for line in entry_list:

        current_line = []
        result = re.search(pattern, line)
        x1, y1, x2, y2 = int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4))
        if max(x1, x2) > max_x:
            max_x = max(x1, x2)
        if max(y1, y2) > max_y:
            max_y = max(y1, y2)

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                current_line.append([x1, y])
            lines.append(current_line)

        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                current_line.append([x, y1])
            lines.append(current_line)

        elif diagonal:
            if x1 > x2:
                x_range = range(x1, x2-1, -1)
            else:
                x_range = range(x1, x2+1)
            if y1 > y2:
                y_range = range(y1, y2-1, -1)
            else:
                y_range = range(y1, y2+1)
            for x, y in zip(x_range, y_range):
                current_line.append([x, y])
            lines.append(current_line)

    grid = np.zeros(shape=(max_y+1, max_x+1))

    for line in lines:
        for point in line:
            grid[point[1], point[0]] += 1

    return np.sum(grid >= 2)


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {hydro(entries, False)}')
print(f'Solution part 2: {hydro(entries, True)}')
