###############################################
# Advent of Code 2023, Day ten: "pipe maze"   #
# https://adventofcode.com/2023/day/10        #
###############################################
    
import os
import numpy as np
from skimage.segmentation import flood_fill
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day10.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------

pipes = {
            '|': np.array([[1, 0], [1, 0]]),
            '-': np.array([[0, 1], [0, 1]]),
            'L': np.array([[1, 0], [0, 1]]),
            'J': np.array([[1, 0], [0, -1]]),
            '7': np.array([[0, 1], [1, 0]]),
            'F': np.array([[0, -1], [1, 0]]),
            '.': None
             }


def step(plan, current_idx, direction):
    new_idx = current_idx + direction
    if np.any(new_idx < 0):
        return None
    current_pipe = plan[tuple(new_idx)]
    if current_pipe == '.':
        return None
    if current_pipe == 'S':
        return 'end_reached'
    reachable = (np.all(direction == pipes[current_pipe][0])
                 or np.all(direction == -pipes[current_pipe][1]))

    if reachable:
        if np.all(direction == pipes[current_pipe][0]):
            next_step = pipes[current_pipe][1]
        else:
            next_step = -pipes[current_pipe][0]
        return new_idx, next_step
    else:
        return None


def run(plan, start_idx):
    step_plans = []
    for start_step in [np.array([0, -1]), np.array([0, 1]), np.array([-1, 0]), np.array([1, 0])]:
        current_idx = start_idx
        step_plan = np.ones_like(plan, dtype=int) * -1
        step_plan[tuple(start_idx)] = 0
        n_steps = 0
        next_step = start_step
        next_state = (current_idx, next_step)
        started = True
        while True:
            c_idx, n_st = next_state
            next_state = step(plan, c_idx, n_st)
            n_steps += 1
            if (next_state is None) or (next_state == 'end_reached'):
                if n_steps == 1:
                    started = False
                break
            step_plan[tuple(next_state[0])] = n_steps

        if started:
            step_plans.append(step_plan)

    return step_plans


def part1(entry_list):

    plan = []
    for line in entry_list:
        plan.append(list(line.strip()))
    plan = np.array(plan)
    start_idx = np.array(np.where(plan == 'S')).squeeze()
    steps = run(plan, start_idx)
    all_paths = np.min(np.concatenate(np.expand_dims(steps, axis=3), axis=2), axis=2)

    path_map = np.pad(np.array((all_paths > 0), dtype=int), (1,1))
    flooded = flood_fill(path_map, (0, 0), 10, connectivity=1)
    flooded = flood_fill(flooded, (100, 30), 10, connectivity=1)

    result_1 = np.max(all_paths)
    result_2 = np.sum(flooded != 10)

    return result_1, result_2


# Solutions ------------------------------------------------------------------------------------------------------------

results = part1(entries)
print(f'Solution part 1: {results[0]}')
print(f'Solution part 2: {results[1]}')
