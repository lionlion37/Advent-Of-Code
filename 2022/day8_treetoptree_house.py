#########################################################
# Advent of Code 2022, Day eight: "TreetopTree House"   #
# https://adventofcode.com/2022/day/8                   #
#########################################################

import os
import numpy as np

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'day8.txt'), 'r') as f:
    entries = f.readlines()

input_grid = np.array([[[int(height), False, 0] for height in line[:-1]] for line in entries])

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(heights):
    n_visible = 2*heights.shape[0] + 2*heights.shape[1] - 4
    heights[0, :, 1] = True
    heights[-1, :, 1] = True
    heights[:, 0, 1] = True
    heights[:, -1, 1] = True

    for y in range(len(heights)):
        horizontal = heights[y]
        heights[y, 0, 1], heights[y, -1, 1] = True, True

        # from left to right
        max_height = horizontal[0, 0]
        for x, tree in enumerate(horizontal[:-1]):
            if tree[0] > max_height:
                max_height = tree[0]
                if not tree[1]:
                    n_visible += 1
                    heights[y, x, 1] = True
        horizontal = heights[y]

        # from right to left
        max_height = horizontal[-1, 0]
        for x, tree in enumerate(horizontal[:0:-1]):
            if tree[0] > max_height:
                max_height = tree[0]
                if not tree[1]:
                    n_visible += 1
                    heights[y, len(horizontal) - 1 - x, 1] = True

    for x in range(len(np.swapaxes(heights, 0, 1))):
        vertical = np.swapaxes(heights, 0, 1)[x]
        heights[0, x, 1], heights[-1, x, 1] = True, True

        # from top to bottom
        max_height = vertical[0, 0]
        for y, tree in enumerate(vertical[:-1]):
            if tree[0] > max_height:
                max_height = tree[0]
                if not tree[1]:
                    n_visible += 1
                    heights[y, x, 1] = True
        vertical = np.swapaxes(heights, 0, 1)[x]

        # bottom to top
        max_height = vertical[-1, 0]
        for y, tree in enumerate(vertical[:0:-1]):
            if tree[0] > max_height:
                max_height = tree[0]
                if not tree[1]:
                    n_visible += 1
                    heights[len(vertical) - 1 - y, x, 1] = True

    return n_visible


def part2(heights):
    scores = []
    for y, line in enumerate(heights):
        if y == 0 or y == len(heights) - 1:
            continue
        for x, tree in enumerate(line):
            if x == 0 or x == len(line) - 1:
                continue
            current_height = tree[0]

            # to the left
            m1 = 0
            for n_x in range(x-1, -1, -1):
                if heights[y, n_x, 0] >= current_height:
                    m1 += 1
                    break
                m1 += 1
            # to the right
            m2 = 0
            for n_x in range(x+1, len(line)):
                if heights[y, n_x, 0] >= current_height:
                    m2 += 1
                    break
                m2 += 1
            # up
            m3 = 0
            for n_y in range(y-1, -1, -1):
                if heights[n_y, x, 0] >= current_height:
                    m3 += 1
                    break
                m3 += 1
            # down
            m4 = 0
            for n_y in range(y+1, len(heights)):
                if heights[n_y, x, 0] >= current_height:
                    m4 += 1
                    break
                m4 += 1
            score = m1 * m2 * m3 * m4
            scores.append(score)
            heights[y, x, 2] = score

    return max(scores)


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(input_grid)}')
print(f'Solution part 2: {part2(input_grid)}')
