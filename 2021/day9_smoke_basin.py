##################################################
# Advent of Code 2021, Day nine: "Smoke Basin"   #
# https://adventofcode.com/2021/day/9            #
##################################################
    
import os
import numpy as np
from collections import deque
import seaborn as sns
import matplotlib.pyplot as plt
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day9.txt'), 'r') as f:
    entries = f.readlines()
entries = np.array([list(map(int, line[:-1])) for line in entries])

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def visualize(entry_list):
    sns.heatmap(data=entry_list, cmap="YlGnBu")
    plt.show()


class Location:

    def __init__(self, coordinates, value, grid):
        self.y, self.x = coordinates
        self.value = value
        self.shape = grid.shape
        self.grid = grid

    def get_successors(self):
        adjacent = [None, None, None, None]  # [Left, Up, Down, Right]
        if self.x > 0:
            adjacent[0] = [self.y, self.x-1]
        if self.x < self.shape[1]-1:
            adjacent[3] = [self.y, self.x+1]
        if self.y > 0:
            adjacent[2] = [self.y-1, self.x]
        if self.y < self.shape[0]-1:
            adjacent[1] = [self.y+1, self.x]

        successors = []
        for r in adjacent:
            if not (r is None):
                successors.append(Location(r, self.grid[r[0], r[1]], self.grid))

        return adjacent, successors


def part1(entry_list):
    risk_level = 0
    low_points = []

    for y in range(len(entry_list)):
        for x in range(len(entry_list[y])):

            location = Location([y, x], entry_list[y, x], entry_list)
            adjacents = []
            for successor in location.get_successors()[1]:
                adjacents.append(successor.value)
            adjacents = np.array(adjacents)

            if not (False in np.array(adjacents > entry_list[y, x])):
                risk_level += entry_list[y, x] + 1
                low_points.append([y, x])

    return risk_level, low_points


def calculate_basin_size(starting_point):

    closed = set()
    fringe = deque()
    fringe.append(starting_point)  # start node = lowest point

    while len(fringe) > 0:

        current = fringe.popleft()

        # check current node
        if current.value == 9:
            continue

        # expand if not already visited
        if (current.y, current.x) not in closed:
            closed.add((current.y, current.x))
            for successor in current.get_successors()[1]:
                fringe.append(successor)

    return len(closed)


def part2(entry_list):
    low_points = part1(entry_list)[1]
    sizes = []
    for lp in low_points:
        current_location = Location(lp, entry_list[lp[0], lp[1]], entry_list)
        sizes.append(calculate_basin_size(current_location))
    sizes = np.array(sizes)

    return np.product(sizes[np.argsort(sizes)[-3:]])


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part1(entries)[0]}')
print(f'Solution part 2: {part2(entries)}')
