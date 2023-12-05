######################################################
# Advent of Code 2023, Day five: "seed fertilizer"   #
# https://adventofcode.com/2023/day/5                #
######################################################
    
import os
import numpy as np


def to_matrix(m):
    _, m = m.split(':')
    rows = m.strip().split('\n')
    matrix = np.array([r.split() for r in rows], dtype=int)
    return matrix


# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day5.txt'), 'r') as f:
    entries = f.read()
    splits = entries.split('\n\n')
    seeds, maps = splits[0], splits[1:]
    seeds = np.array(seeds[6:].split(), dtype=int)
    maps = [to_matrix(mp) for mp in maps]
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(seeds, maps):

    locations = []
    for seed in seeds:
        current_idx = seed
        for mp in maps:
            mp_search = np.where((current_idx >= mp[:, 1]) * (current_idx < mp[:, 1] + mp[:, 2]))[0]
            if len(mp_search) > 0:
                mp_line = mp[mp_search[0]]
                current_idx = mp_line[0] + current_idx - mp_line[1]
            else:
                continue
        locations.append(current_idx)

    return min(locations)


    
def part2(seeds, maps):
    maps = maps[::-1]
    intervals = seeds.reshape(-1, 2)

    found = False
    seed = -1
    while not found:
        seed += 1
        current_idx = seed
        for mp in maps:
            mp_search = np.where((current_idx >= mp[:, 0]) * (current_idx < mp[:, 0] + mp[:, 2]))[0]
            if len(mp_search) > 0:
                mp_line = mp[mp_search[0]]
                current_idx = mp_line[1] + current_idx - mp_line[0]
            else:
                continue
        if np.sum((current_idx >= intervals[:, 0]) * (current_idx < intervals[:, 0] + intervals[:, 1])) > 0:
            found = True

    return seed


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(seeds, maps)}')
print(f'Solution part 2: {part2(seeds, maps)}')
