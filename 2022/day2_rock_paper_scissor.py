########################################################
# Advent of Code 2022, Day two: "Rock Paper Scissor"   #
# https://adventofcode.com/2022/day/2                  #
########################################################

import os

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'day2.txt'), 'r') as f:
    entries = f.readlines()


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list):
    score = 0
    points = {'A X': 4, 'A Y': 8, 'A Z': 3,
              'B X': 1, 'B Y': 5, 'B Z': 9,
              'C X': 7, 'C Y': 2, 'C Z': 6}
    for game in entry_list:
        score += points[game[:-1]]

    return score


def part2(entry_list):
    score = 0
    points = {'A X': 3, 'A Y': 4, 'A Z': 8,
              'B X': 1, 'B Y': 5, 'B Z': 9,
              'C X': 2, 'C Y': 6, 'C Z': 7}

    for game in entry_list:
        score += points[game[:-1]]

    return score


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
