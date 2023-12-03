##################################################################
# Advent of Code 2021, Day fourteen: "Extended Polymerization"   #
# https://adventofcode.com/2021/day/14                           #
##################################################################

import os

# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day14.txt'), 'r') as f:
    entries = f.readlines()

initial_state = entries[0][:-1]
rule_pairs = [entry.split(' -> ')[0] for entry in entries[2:]]
rule_inserts = [entry[:-1].split(' -> ')[1] for entry in entries[2:]]

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def polymerize(state, rules, n):

    # initialize
    pairs, inserts = rules
    # number of elements occurrences
    elements = dict()
    for el in set(list(state)):
        elements[el] = state.count(el)
    # number of pair occurrences
    n_pairs = dict()
    for pair in pairs:
        n_pairs[pair] = state.count(pair)

    # run for n steps
    for _ in range(n):

        current_n_pairs = n_pairs.copy()

        for insert, pair in zip(inserts, pairs):

            n_appearances = n_pairs[pair]

            # update pairs
            if pair[0] + insert in n_pairs.keys():
                current_n_pairs[pair[0] + insert] += n_appearances
            if insert + pair[1] in n_pairs.keys():
                current_n_pairs[insert + pair[1]] += n_appearances
            current_n_pairs[pair] -= n_appearances

            # update elements
            if not insert in elements.keys():
                elements[insert] = n_appearances
            else:
                elements[insert] += n_appearances

        n_pairs = current_n_pairs.copy()

    return max(elements.values()) - min(elements.values())


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {polymerize(initial_state, (rule_pairs, rule_inserts), 10)}')
print(f'Solution part 2: {polymerize(initial_state, (rule_pairs, rule_inserts), 40)}')
