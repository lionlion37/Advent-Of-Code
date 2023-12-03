################################################
# Advent of Code 2021, Day fifteen: "Chiton"   #
# https://adventofcode.com/2021/day/15         #
################################################

import os
from queue import PriorityQueue
import numpy as np

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'day15.txt'), 'r') as f:
    entries = f.readlines()
entries = [[int(n) for n in entry[:-1]] for entry in entries]


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def get_successors(entry_list, node):
    y, x = node
    shape = (len(entry_list), len(entry_list[-1]))
    successors = []
    if y > 0:
        successors.append((entry_list[y, x], (y - 1, x)))
    if x > 0:
        successors.append((entry_list[y, x], (y, x - 1)))
    if x < shape[1] - 1:
        successors.append((entry_list[y, x], (y, x + 1)))
    if y < shape[0] - 1:
        successors.append((entry_list[y, x], (y + 1, x)))

    return successors


def part1(entry_list, visualize=False):
    closed = set()
    goal_idx = (len(entry_list) - 1, len(entry_list[-1]) - 1)
    fringe = PriorityQueue()

    fringe.put((0, (0, 0), [(0, 0)]))  # (cumulative_cost, current_node)

    while not fringe.empty():
        cumulative_cost, node, path = fringe.get()

        if node == goal_idx:
            cost = 0
            for p in path:
                cost += entry_list[p[0], p[1]]

            if visualize:
                for y in range(len(entry_list)):
                    output = ""
                    for x in range(len(entry_list[0])):
                        if (y, x) in path:
                            output += str(entry_list[y, x])
                        else:
                            output += "."
                    print(output)

            return cost - entry_list[0, 0]

        if not (node in closed):
            closed.add(node)
            for successor in get_successors(entry_list, node):
                if not (successor[1] in closed):
                    fringe.put(((successor[0] + cumulative_cost), successor[1], path + [successor[1]]))

    return False


def part2(entry_list, visualize=False):
    entry_list = np.array(entry_list)
    full_map = np.concatenate((
        np.concatenate((entry_list, entry_list + 1, entry_list + 2, entry_list + 3, entry_list + 4), axis=1),
        np.concatenate((entry_list, entry_list + 1, entry_list + 2, entry_list + 3, entry_list + 4), axis=1) + 1,
        np.concatenate((entry_list, entry_list + 1, entry_list + 2, entry_list + 3, entry_list + 4), axis=1) + 2,
        np.concatenate((entry_list, entry_list + 1, entry_list + 2, entry_list + 3, entry_list + 4), axis=1) + 3,
        np.concatenate((entry_list, entry_list + 1, entry_list + 2, entry_list + 3, entry_list + 4), axis=1) + 4))
    full_map[full_map == 10] = 1
    full_map[full_map == 11] = 2
    full_map[full_map == 12] = 3
    full_map[full_map == 13] = 4
    full_map[full_map == 14] = 5
    full_map[full_map == 15] = 6
    full_map[full_map == 16] = 7
    full_map[full_map == 17] = 8
    full_map[full_map == 18] = 9
    print("Starting search...")
    cost = part1(full_map, visualize=visualize)

    return cost


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(np.array(entries))}')
print(f'Solution part 2: {part2(entries)}')
