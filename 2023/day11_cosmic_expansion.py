#########################################################
# Advent of Code 2023, Day eleven: "cosmic expansion"   #
# https://adventofcode.com/2023/day/11                  #
#########################################################

import os
import numpy as np
import collections
from tqdm import tqdm

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'day11.txt'), 'r') as f:
    input_plan = []
    raw = f.readlines()
    for line in raw:
        input_plan.append(list(line.strip()))
    input_plan = np.array(input_plan)


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


class Node:
    def __init__(self, plan, idx, start_node=False):
        self.plan = plan
        self.idx = np.array(idx)
        self.value = self.plan[tuple(idx)]
        self.start_node = start_node

    def get_neighbors(self):
        for direction in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            new_idx = self.idx + np.array(direction)
            if (np.any(new_idx < 0) or
                    (new_idx[0] >= self.plan.shape[0] or new_idx[1] >= self.plan.shape[1])):
                continue
            else:
                yield Node(self.plan, new_idx)


def bfs(plan):
    n_galaxies = np.sum(plan == '#')
    dist_matrix = np.zeros((n_galaxies, n_galaxies))
    dist_matrix[:, :] = np.inf
    for n_galaxy in tqdm(range(n_galaxies)):
        y_len, x_len = plan.shape

        flat_idx = np.where(plan.flatten() == '#')[0][n_galaxy]
        root_idx = (flat_idx // x_len, flat_idx % x_len)

        root_node = Node(plan, root_idx, start_node=True)

        visited, queue = set(), collections.deque()
        queue.append([root_node])
        visited.add(tuple(root_node.idx))

        while queue:
            path = queue.popleft()
            vertex = path[-1]

            if vertex.value == '#' and not vertex.start_node:
                flat_idx = x_len * vertex.idx[0] + vertex.idx[1]
                end_idx = np.where(np.where(plan.flatten() == '#')[0] == flat_idx)
                if dist_matrix[n_galaxy, end_idx] > len(path) - 1:
                    dist_matrix[n_galaxy, end_idx] = len(path) - 1

            for neighbor in vertex.get_neighbors():
                if tuple(neighbor.idx) not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    visited.add(tuple(neighbor.idx))
                    queue.append(new_path)

    half_dist_matrix = np.tril(dist_matrix)
    half_dist_matrix[half_dist_matrix == np.inf] = 0

    return int(np.sum(half_dist_matrix))


def solve(plan, n_expansions):
    result = 0
    galaxy_idx = np.concatenate(np.expand_dims(np.where(plan == '#'), axis=2), axis=1)

    y = 0
    for line in plan:
        if '#' not in line:
            galaxy_idx[np.where(galaxy_idx[:, 0] > y)[0], 0] += n_expansions
            y += n_expansions + 1
        else:
            y += 1

    x = 0
    for col in plan.T:
        if '#' not in col:
            galaxy_idx[np.where(galaxy_idx[:, 1] > x)[0], 1] += n_expansions
            x += n_expansions + 1
        else:
            x += 1

    for n, galaxy in enumerate(galaxy_idx):
        for partner_gal in galaxy_idx[n:]:
            manhattan = np.sum(np.abs(galaxy - partner_gal))
            result += manhattan

    return result

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {solve(input_plan, 1)}')
print(f'Solution part 2: {solve(input_plan, 999999)}')
