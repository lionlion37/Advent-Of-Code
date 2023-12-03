########################################################
# Advent of Code 2020, Day Seven: "Handy Haversacks"   #
# https://adventofcode.com/2020/day/7                  #
########################################################

import os
from day7_utils import rule_getter, gold_finder, find_num_bags

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
with open(os.path.join('inputs', 'day7.txt'), 'r') as f:
    entry_list = f.readlines()

test_entry = ['light red bags contain 1 bright white bag, 2 muted yellow bags.\n',
              'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n',
              'bright white bags contain 1 shiny gold bag.\n',
              'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n',
              'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n',
              'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n',
              'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n',
              'faded blue bags contain no other bags.\n',
              'dotted black bags contain no other bags.']

test_entry_2 = ['shiny gold bags contain 2 dark red bags.\n',
                'dark red bags contain 2 dark orange bags.\n',
                'dark orange bags contain 2 dark yellow bags.\n',
                'dark yellow bags contain 2 dark green bags.\n',
                'dark green bags contain 2 dark blue bags.\n',
                'dark blue bags contain 2 dark violet bags.\n',
                'dark violet bags contain no other bags.\n']

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entries):
    """
    Returns the number of bags that contain at least one shiny gold bag for a given list of rules.
    :param entries: list of rules
    :return: number of bags that contain at least one shiny gold bag
    """
    rc, _ = rule_getter(entries)
    n_gold = 0

    for bag in rc:
        if gold_finder(bag, rc):
            n_gold += 1

    return n_gold


def part2(entries):
    """
    Returns the number of bags contained in a shiny gold bag for a given list of rules.
    :param entries: list of rules
    :return: the number of bags contained in a shiny gold bag
    """
    _, rc = rule_getter(entries)
    return find_num_bags('shiny gold', rc)


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part1(entry_list)}')
print(f'Solution part 2: {part2(entry_list)}')
