##############################################################
# Advent of Code 2021, Day thirteen: "Transparent Origami"   #
# https://adventofcode.com/2021/day/13                       #
##############################################################
    
import os
import re
import numpy as np
import time
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day13_custom.txt'), 'r') as f:
    entries = f.readlines()

initial_dots = set()
start_instructions = []
pattern = 'fold along (x|y)=(\d+)'
c_dict = {'x': 0, 'y': 1}

for entry in entries:
    if entry != "\n" and not ('fold' in entry):
        x, y = entry.split(',')
        initial_dots.add(tuple((int(x), int(y))))
    elif 'fold' in entry:
        result = re.search(pattern, entry)
        start_instructions.append([c_dict[result.group(1)], int(result.group(2))])

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def fold(dots: set, instructions, render_all=False, render_end=False, end_after=None):

    current_dots = dots.copy()
    for n, instruction in enumerate(instructions):
        if n == end_after:
            break
        axis, c_fold = instruction
        folded_dots = set()
        for dot in current_dots:
            if dot[axis] > c_fold:
                new_dot = [0, 0]
                new_dot[axis] = 2 * c_fold - dot[axis]
                new_dot[not axis] = dot[not axis]
                folded_dots.add(tuple(new_dot))
            else:
                folded_dots.add(dot)

        current_dots = folded_dots

        if render_all:
            os.system('clear')
            if not n == len(instructions) - 1:
                render_dots(current_dots, instructions[n + 1])
            else:
                render_dots(current_dots, instructions[n])
            time.sleep(0.5)

    if render_end and not render_all:
        render_dots(current_dots)

    return len(current_dots)


def render_dots(current_dots, next_instruction=None):

    dots_render = []
    for dot in current_dots:
        dots_render.append([dot[0], dot[1]])
    dots_render = np.array(dots_render)
    if next_instruction:
        axis, c_fold = next_instruction
        fold_symbol = '\u2503' if axis == 0 else '\u2501'

    for y in range(np.max(dots_render[:, 1]) + 1):
        current_line = ""
        for x in range(np.max(dots_render[:, 0]) + 1):

            if next_instruction:
                current_coordinate = (x,y)
                fold_point = [0,0]
                fold_point[axis] = c_fold
                fold_point[not axis] = current_coordinate[not axis]
                if (x,y) == tuple(fold_point):
                    current_line += fold_symbol

            if (x,y) in current_dots:
                current_line += "\u2588"
            else:
                current_line += " "
        print(current_line)


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {fold(initial_dots, start_instructions, end_after=1)}')
fold(initial_dots, start_instructions, render_end=True)  # Part 2
