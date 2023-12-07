################################################
# Advent of Code 2023, Day six: "Wait Forit"   #
# https://adventofcode.com/2023/day/6          #
################################################
    
import os
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------

races_part1 = [[48, 255], [87, 1288], [69, 1117], [81, 1623]]
races_part2 = [[48876981, 255128811171623]]
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def calc(races):
    result = 1
    for race in races:
        T, S = race
        t1 = (-T - np.sqrt(T**2 - 4*S)) / (-2)
        t2 = (-T + np.sqrt(T**2 - 4*S)) / (-2)
        if int(min(t1, t2)) == min(t1, t2):
            left = min(t1, t2) + 1
        else:
            left = int(min(t1, t2) + 1)
        if int(max(t1, t2)) == max(t1, t2):
            right = max(t1, t2) - 1
        else:
            right = int(max(t1, t2))
        result *= (right - left + 1)

    return result


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {calc(races_part1)}')
print(f'Solution part 2: {calc(races_part2)}')
