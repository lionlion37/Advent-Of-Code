###################################################
# Advent of Code 2023, Day three: "Gear Ratios"   #
# https://adventofcode.com/2023/day/3             #
###################################################
    
import os
import re
import numpy as np

# get input ------------------------------------------------------------------------------------------------------------

engine = []
with open(os.path.join('inputs', 'day3.txt'), 'r') as f:
    for line in f:
        engine.append(list(line[:-1]))
engine = np.array(engine)
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(engine):
    result_1 = 0
    result_2 = 0
    pattern = '[^\d\.]'
    found_parts = set()
    for y, line in enumerate(engine):
        for match in re.finditer(pattern, ''.join(line)):
            gear = False
            x = match.start(0)
            if ''.join(line)[x] == '*':
                gear = True
            y_lower, y_upper = max(0, y-1), min(y+2, len(engine))
            x_lower, x_upper = max(0, x-1), min(x+2, len(engine[0]))
            neighborhood = engine[y_lower:y_upper, x_lower:x_upper]
            numbers = []
            for num_match in re.finditer('\d+', '.'.join([''.join(l) for l in neighborhood]) + '.'):
                found = False
                y_idx = int(num_match.start(0) / (x_upper - x_lower + 1))
                x_idx = int(num_match.start(0) - (x_upper - x_lower + 1) * y_idx)
                y_idx += y_lower
                x_idx += x_lower
                if (y_idx, x_idx) in found_parts:
                    continue
                else:
                    found_parts.add((y_idx, x_idx))
                number = engine[y_idx, x_idx]

                current_x = x_idx - 1
                while current_x >= 0 and re.search('\d', engine[y_idx, current_x]) and not found:
                    if (y_idx, current_x) in found_parts:
                        found = True
                    else:
                        found_parts.add((y_idx, current_x))
                    number = engine[y_idx, current_x] + number
                    current_x -= 1

                if found:
                    continue

                current_x = x_idx + 1
                while current_x < len(engine[0]) and re.search('\d', engine[y_idx, current_x]) and not found:
                    if (y_idx, current_x) in found_parts:
                        found = True
                    else:
                        found_parts.add((y_idx, current_x))
                    number = number + engine[y_idx, current_x]
                    current_x += 1

                if found:
                    continue

                result_1 += int(number)
                numbers.append(number)

            if gear and len(numbers) == 2:
                result_2 += int(numbers[0]) * int(numbers[1])

    return result_1, result_2


# Solutions ------------------------------------------------------------------------------------------------------------

results = part1(engine)
print(f'Solution part 1: {results[0]}')
print(f'Solution part 2: {results[1]}')
