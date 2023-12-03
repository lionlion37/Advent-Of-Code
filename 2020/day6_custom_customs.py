####################################################
# Advent of Code 2020, Day Six: "Custom Customs"   #
# https://adventofcode.com/2020/day/6              #
####################################################

import os

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
with open(os.path.join('inputs', 'day6.txt'), 'r') as f:
    entry_list = f.readlines()

test_entry = ['abc\n', '\n', 'a\n', 'b\n', 'c\n', '\n', 'ab\n', 'ac\n', '\n', 'a\n', 'a\n', 'a\n', '\n', 'b']

# function for part 1 and part 2 of the puzzle -------------------------------------------------------------------------


def count_positive_answers(entries):
    """
    Takes batches of strings as input where each batch is separated by a '\n' line. Counts (1) the total number of
    distinct characters per batch and (2) the total number of characters which appear in every line of one batch.
    :param entries: list of character strings in batches where the batches are separated by blank lines
    :return: n_yes_any: sum of numbers of distinct characters per batch, n_yes_every: sum of numbers of characters per
    batch that appear in each line of a batch
    """
    entries.append('\n')
    questions_yes = {}
    n_yes_any = 0
    n_yes_every = 0
    n_people = 0

    for n, line in enumerate(entries):

        if line == '\n':
            for k in questions_yes:
                if questions_yes[k] == n_people:
                    n_yes_every += 1
            questions_yes = {}
            n_people = 0

        else:
            n_people += 1
            for q in line:
                if q != '\n' and q not in questions_yes.keys():
                    questions_yes[q] = 1
                    n_yes_any += 1
                elif q != '\n' and q in questions_yes.keys():
                    questions_yes[q] += 1

    return n_yes_any, n_yes_every


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {count_positive_answers(entry_list)[0]}')
print(f'Solution part 2: {count_positive_answers(entry_list)[1]}')
