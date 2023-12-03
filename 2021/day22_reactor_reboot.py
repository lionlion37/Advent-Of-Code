##########################################################
# Advent of Code 2021, Day twentytwo: "Reactor Reboot"   #
# https://adventofcode.com/2021/day/22                   #
##########################################################
    
import os
import portion as P
import re
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day22.txt'), 'r') as f:
    entries = f.readlines()
pattern = '(on|off) x=(-?\\d*)..(-?\\d*),y=(-?\\d*)..(-?\\d*),z=(-?\\d*)..(-?\\d*)\n'
interval_list = []
for entry in entries:
    result = re.search(pattern, entry)
    interval_list.append([int(result.group(1) == 'on'), int(result.group(2)), int(result.group(3)), int(result.group(4)),
                          int(result.group(5)), int(result.group(6)), int(result.group(7))])

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def get_cuboid_size(x, y, z):
    return len(list(P.iterate(x, 1))) * len(list(P.iterate(y, 1))) * len(list(P.iterate(z, 1)))


def part1(interval_list):
    cubes = set()
    for interval in interval_list:
        if interval[0] == 1:
            for x in range(interval[1], interval[2]+1):
                for y in range(interval[3], interval[4]+1):
                    for z in range(interval[5], interval[6]+1):
                        cubes.add((x, y, z))

        else:
            for x in range(interval[1], interval[2]+1):
                for y in range(interval[3], interval[4]+1):
                    for z in range(interval[5], interval[6]+1):
                        if (x, y, z) in cubes:
                            cubes.remove((x, y, z))

    return len(cubes)


    
def part2(entry_list):


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(interval_list)}')
# print(f'Solution part 2: {part2(entries)}')
