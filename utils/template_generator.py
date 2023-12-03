def template_generator(day_number, day_number_word, puzzle_name_1, puzzle_name_2, int_input):

    len_header = 36 + len(day_number_word) + len(puzzle_name_1) + len(puzzle_name_2)

    if int_input == "True":
        to_int = "\nentries = [int(entry) for entry in entries]"
    else:
        to_int = ""

    str_to_write = "#" * len_header + f"""
# Advent of Code YEAR, Day {day_number_word}: "{puzzle_name_1} {puzzle_name_2}"   #
# https://adventofcode.com/YEAR/day/{day_number}""" + " " * (len(day_number_word) + len(puzzle_name_1) +
                                                                  len(puzzle_name_2) - 1 - len(day_number)) \
                   + "#\n" + "#" * len_header + f"""
    
import os
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day{day_number}.txt'), 'r') as f:
    entries = f.readlines(){to_int}
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entry_list):
    pass
    
    
def part2(entry_list):
    pass

# Solutions ------------------------------------------------------------------------------------------------------------
""" + """

# print(f'Solution part 1: {part1(entries)}')
# print(f'Solution part 2: {part2(entries)}')
"""

    with open('day' + day_number + '_' + puzzle_name_1.lower() + '_' + puzzle_name_2.lower() + '.py',
              'w') as f:
        f.write(str_to_write)
