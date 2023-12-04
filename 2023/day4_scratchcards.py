#####################################################
# Advent of Code 2023, Day four: "Scratchcards _"   #
# https://adventofcode.com/2023/day/4               #
#####################################################
    
import os
import re
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day4.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def solve(entry_list):
    result_1 = 0
    cards_counter = np.ones(len(entry_list))
    for n, card in enumerate(entry_list):
        card = card.replace('  ', ' ')
        _, numbers = card.split(':')
        winning_n, my_n = numbers.strip().split('|')
        winning_n, my_n = np.array(winning_n.strip().split(' '), dtype=int), np.array(my_n.strip().split(' '), dtype=int)
        n_matches = np.sum(list(map(lambda x: x in winning_n, my_n)))

        if n_matches > 0:  # part 1
            result_1 += np.power(2, n_matches-1)

        cards_counter[n + 1:n + 1 + n_matches] += cards_counter[n]  # part 2
        result_2 = int(np.sum(cards_counter))

    return result_1, result_2


# Solutions ------------------------------------------------------------------------------------------------------------

results = solve(entries)
print(f'Solution part 1: {results[0]}')
print(f'Solution part 2: {results[1]}')
