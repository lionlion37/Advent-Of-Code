########################################################
# Advent of Code 2020, Day Seventeen: "Conway Cubes"   #
# https://adventofcode.com/2020/day/17                 #
########################################################

import os
import numpy as np
import copy

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'day17.txt'), 'r') as f:
    entry_list = []
    for line in f.readlines():
        entry_list.append(list(line[:-1]))

test_entry = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def pad_dim_p(dim_list, p) -> list:
    output = []
    for d in range(len(dim_list) + p * 2):
        output.append([[0] * (len(dim_list[0]) + p * 2)] * p)
        if d <= p - 1 or d >= len(dim_list) + p:
            for _ in range(len(dim_list[0])):
                output[d].append([0] * (len(dim_list[0][0]) + p * 2))
        else:
            for line in dim_list[d - p]:
                output[d].append([0] * p + line + [0] * p)
        for _ in range(p):
            output[d].append([0] * (len(dim_list[0]) + p * 2))

    return output


def cycle_once(dim_list):
    temp_np = np.array(copy.deepcopy(dim_list))
    output = np.array(copy.deepcopy(dim_list))
    for z in range(0, len(dim_list)):
        for y in range(0, len(dim_list[0])):
            for x in range(0, len(dim_list)):
                neighbourhood = temp_np[z - 1:z + 2, y - 1:y + 2, x - 1:x + 2]
                n_active = np.count_nonzero(neighbourhood == 1)
                if temp_np[z, y, x] == 1:
                    if n_active - 1 == 2 or n_active - 1 == 3:
                        continue
                    else:
                        output[z, y, x] = 0
                else:
                    if n_active == 3:
                        output[z, y, x] = 1
    output = pad_dim_p(output.tolist(), 15)
    output = np.array(output)
    return output


def part1(entries):
    dimension = [[[]]]
    for n, l in enumerate(entries):
        while len(dimension[0]) - 1 < n:
            dimension[0].append([])
        for m, el in enumerate(l):
            while len(dimension[0][n]) - 1 < m:
                dimension[0][n].append(0)
            dimension[0][n][m] = int((el == '#'))
    dim_paded = pad_dim_p(dimension, 15)
    state = cycle_once(dim_paded)
    for _ in range(5):
        state = cycle_once(state)
    state_np = np.array(state)
    n_active = np.count_nonzero(state_np == 1)
    return n_active


# Solutions ------------------------------------------------------------------------------------------------------------

a = part1(entry_list)
print('Done')
