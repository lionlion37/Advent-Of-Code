##################################################
# Advent of Code 2021, Day four: "Giant Squid"   #
# https://adventofcode.com/2021/day/4            #
##################################################

import os
import numpy as np

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'day4.txt'), 'r') as f:
    entries = f.readlines()


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def bingo(entry_list):
    draws = entry_list[0][:-1].split(",")
    boards, current_board = [], []
    winners, winning_draws = [], []

    for line in entry_list[2:]:
        if line == "\n":
            boards.append(current_board)
            current_board = []
        else:
            current_board.append(line.split())
    boards = np.array(boards)

    draw_mask = np.array(boards == draws[0])
    for draw in draws[1:]:
        if len(winners) == len(boards):
            break
        draw_mask += np.array(boards == draw)
        for n, mask in enumerate(draw_mask):
            if n in winners:
                continue
            for index in range(5):
                if (not (False in np.array(mask[:, index]))) or (not (False in mask[index])):
                    winners.append(n)
                    winning_draws.append(draw)
                    if len(winners) == 1:
                        first_unmarked_mask = np.array(draw_mask[winners[0]] == False)
                    break

    last_board = boards[winners[-1]]
    last_unmarked_mask = np.array(draw_mask[winners[-1]] == False)
    last_unmarked_sum = np.sum(np.array(last_board[last_unmarked_mask], dtype=int))

    winning_board = boards[winners[0]]
    first_unmarked_sum = np.sum(np.array(winning_board[first_unmarked_mask], dtype=int))

    return first_unmarked_sum * int(winning_draws[0]), last_unmarked_sum * int(winning_draws[-1])


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {bingo(entries)[0]}')
print(f'Solution part 2: {bingo(entries)[1]}')
