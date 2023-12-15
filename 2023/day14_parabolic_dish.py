#########################################################
# Advent of Code 2023, Day fourteen: "parabolic dish"   #
# https://adventofcode.com/2023/day/14                  #
#########################################################
    
import os
import numpy as np
from tqdm import tqdm

# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day14.txt'), 'r') as f:
    entries = f.readlines()
    input_plan = []
    for line in entries:
        input_plan.append(list(line.strip()))
    input_plan = np.array(input_plan)

    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def tilt_north(plan):
    result = 0

    for x, col in enumerate(plan.T):

        if 'O' not in col:
            continue

        tmp_col = col.copy()
        tmp_col[np.where(tmp_col == '#')] = 'O'
        rock_idx = np.where(tmp_col == 'O')[0]
        moving_rock_idx = np.where(col == 'O')[0]
        rocks = col[rock_idx]

        plan[moving_rock_idx, x] = '.'

        for n, rock_type in enumerate(rocks):
            if rock_type == '#':
                continue
            else:
                if n == 0:
                    rock_idx[n] = 0
                else:
                    rock_idx[n] = rock_idx[n - 1] + 1

        new_moving_idx = rock_idx[np.where(rocks == 'O')]
        result += np.sum(len(plan) - new_moving_idx)
        plan[new_moving_idx, x] = 'O'

    return result, plan


def part2(plan, cycle_reps):

    hash_cylce_dict = {}
    seen_states = set()
    seen_states.add(hash(tuple([tuple(p) for p in plan])))
    hash_cylce_dict[hash(tuple([tuple(p) for p in plan]))] = 0

    loop_detected = False
    n_cycle = 0
    remaining_cycles = 1

    while remaining_cycles > 0:
        for rot in range(4):
            _, plan = tilt_north(plan)
            plan = np.rot90(plan, 3)

        if not loop_detected:
            state_hash = hash(tuple([tuple(p) for p in plan]))
            n_cycle += 1
            if state_hash in seen_states:
                loop_start = n_cycle + 1
                loop_length = n_cycle - hash_cylce_dict[state_hash]
                loop_detected = True
                remaining_cycles = (cycle_reps - loop_start) % loop_length + 1

            else:
                seen_states.add(state_hash)
                hash_cylce_dict[state_hash] = n_cycle

        else:
            remaining_cycles -= 1

    rock_y = np.where(plan == 'O')[0]
    load = np.sum(len(plan) - rock_y)

    return load


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {tilt_north(input_plan.copy())[0]}')
print(f'Solution part 2: {part2(input_plan.copy(), 1000000000)}')
