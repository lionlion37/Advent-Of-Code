######################################################
# Advent of Code 2021, Day twentythree: "Amphipod"   #
# https://adventofcode.com/2021/day/23               #
######################################################
    
import os
import numpy as np
from queue import PriorityQueue
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day23.txt'), 'r') as f:
    entries = f.readlines()

with open(os.path.join('inputs', 'day23_goal.txt'), 'r') as f:
    goal = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


class Burrow:
    def __init__(self, initial_state, goal_state):
        """
        states:
        0: A
        1: B
        2: C
        3: D
        4: empty space
        5: wall
        """
        self.state_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, '.': 4, '#': 5}
        self.reverse_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: '.', 5: '#'}
        self.cost_dict = {0: 1, 1: 10, 2: 100, 3: 1000}

        self.current_state = np.zeros(shape=(5, 13))
        for y, line in enumerate(initial_state):
            for x, element in enumerate(line[:-1]):
                self.current_state[y, x] = self.state_dict[element]

        self.goal_state = np.zeros(shape=(5, 13))
        for y, line in enumerate(goal_state):
            for x, element in enumerate(line[:-1]):
                self.goal_state[y, x] = self.state_dict[element]

    def get_moves(self, state):
        pods_idx = []
        possible_states = []

        for pod in [0, 1, 2, 3]:
            for idx in np.argwhere(state == pod):
                pods_idx.append([pod, idx])

        for pods in pods_idx:
            type = pods[0]
            pod = pods[1]

            # Rule 2
            corr = self.get_corridor(state)
            rooms = self.get_rooms(state)

            # moves from corridor into room
            if pod[0] == 1:
                next_state = state.copy()

                if rooms[type][0] in [type, 4] and rooms[type][0] in [type, 4]:  # can move in room
                    cost = 0
                    if pod[1] < type + 3:
                        if not state[pod[1]:type+4].tolist() == [4] * (type + 3 - pod[1]):
                            continue
                        cost += self.cost_dict[type] * (type + 3 - pod[1])
                    elif pod[1] > type + 3:
                        if not state[type+3:pod[1]+1].tolist() == [4] * (pod[1] - (type + 3)):
                            continue
                        cost += self.cost_dict[type] * (pod[1] - (type + 3))

                    if rooms[type][1] == type:
                        cost += 1
                        next_state[2, type+3] = type
                    else:
                        cost += 2
                        next_state[3, type+3] = type
                    next_state[pod] = 4
                    possible_states.append([cost, next_state])

                else:
                    continue  # Specific pod cannot move in target room and therefore cannot move at all

            if pod[0] == 3 and state[2, pod[1]] != 4:
                continue

            # moves out of room
            possible_moves = []
            current_s = int(pod[1])-1
            while current_s > 0:
                if corr[current_s-1] == 4:
                    possible_moves.append(current_s)
                    current_s -= 1
                else:
                    break
            current_s = int(pod[1])+1
            while current_s <= len(corr):
                if corr[current_s-1] == 4:
                    possible_moves.append(current_s)
                    current_s += 1
                else:
                    break

            for n in possible_moves:
                next_state = state.copy()
                next_state[1, n] = type
                next_state[pod[0], pod[1]] = 4

                cost = self.cost_dict[type] * abs(pod[1] - n) + pod[0] - 1
                possible_states.append([cost, next_state])

                # elf.render(next_state)
                # print('\n')

        return possible_states

    def render(self, state):
        for line in state:
            result = ""
            for element in line:
                result += self.reverse_dict[element]
            print(result)

    def get_corridor(self, state):
        return state[1, 1:-1]

    def get_rooms(self, state):
        return state[2:4, 3], state[2:4, 5], state[2:4, 7], state[2:4, 9]

    def search(self):
        visited = set()
        fringe = PriorityQueue()
        current = self.current_state
        fringe.put((0, current.tolist()))

        while not fringe.empty():
            cumulative_cost, state = fringe.get()
            print(cumulative_cost)

            if totuple(state) == totuple(self.goal_state):
                return cumulative_cost

            if not totuple(state) in visited:
                visited.add(totuple(state))
                for successor in self.get_moves(np.array(state)):
                    if not totuple(successor[1]) in visited:
                        fringe.put(((cumulative_cost + successor[0]), successor[1].tolist()))

        return False


def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

def part1(entry_list):
    pass
    
    
def part2(entry_list):
    pass

# Solutions ------------------------------------------------------------------------------------------------------------

burrow = Burrow(entries, goal)
print(burrow.search())

# print(f'Solution part 1: {part1(entries)}')
# print(f'Solution part 2: {part2(entries)}')
