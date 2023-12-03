######################################################
# Advent of Code 2021, Day eleven: "Dumbo Octopus"   #
# https://adventofcode.com/2021/day/11               #
######################################################
    
import os
import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day11.txt'), 'r') as f:
    entries = f.readlines()
entries = np.array([list(map(int, line[:-1])) for line in entries])
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


class Octopus:

    def __init__(self, initial_state):
        self.current_state = initial_state
        self.neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        self.energy_size = self.current_state.shape

    def step(self):
        flashed = set()
        synchronized = False

        # update neighbors
        while np.any(self.current_state >= 9):
            flashing = np.argwhere(self.current_state >= 9)
            for flash in np.argwhere(self.current_state >= 9):
                flashed.add(tuple(flash))

            for flash in flashing:

                self.current_state[flash[0], flash[1]] = -1
                for n in self.neighbors:
                    if 0 <= (flash[0] + n[0]) < self.energy_size[0] and 0 <= (flash[1] + n[1]) < self.energy_size[1] \
                            and not ((flash[0] + n[0], flash[1] + n[1]) in flashed):
                        self.current_state[flash[0] + n[0], flash[1] + n[1]] += 1

        self.current_state += 1

        if np.sum(self.current_state) == 0:
            synchronized = True

        return len(flashed), synchronized


def part1(initial_state, n):
    n_flashes = 0
    octopus = Octopus(initial_state)
    for _ in range(n):
        n_flashes += octopus.step()[0]

    return n_flashes


def part2(initial_state):
    n_steps = 0
    octopus = Octopus(initial_state)
    while True:
        n_steps += 1
        if octopus.step()[1]:
            break

    return n_steps

# Solutions ------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    print(f'Solution part 1: {part1(entries.copy(), 100)}')
    print(f'Solution part 2: {part2(entries.copy())}')
