########################################################
# Advent of Code 2021, Day twelve: "Passage Pathing"   #
# https://adventofcode.com/2021/day/12                 #
########################################################
    
import os
from collections import deque, defaultdict
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day12.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def traverse(entry_list, visit_twice=False):

    graph = defaultdict(list)

    for edge in entry_list:
        a, b = edge.rstrip().split('-')

        if b != 'start':
            graph[a].append(b)
        if a != 'start':
            graph[b].append(a)

    n_paths = 0
    double = not visit_twice
    fringe = deque([('start', {'start'}, double)])

    while len(fringe) > 0:

        current, visited, double = fringe.popleft()

        # check current node
        if current == "end":
            n_paths += 1
            continue

        # expand if not already visited
        for neighbor in graph[current]:
            if neighbor not in visited or neighbor.isupper():
                fringe.append((neighbor, visited | {neighbor}, double))
                continue
            if double:
                continue
            fringe.append((neighbor, visited, True))

    return n_paths


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {traverse(entries, False)}')
print(f"Solution part 2: {traverse(entries, True)}")
