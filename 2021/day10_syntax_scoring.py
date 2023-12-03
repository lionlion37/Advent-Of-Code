####################################################
# Advent of Code 2021, Day ten: "Syntax Scoring"   #
# https://adventofcode.com/2021/day/10             #
####################################################
    
import os
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day10.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def syntax_checker(entry_list):
    lefty = "([{<"
    righty = ")]}>"
    score_1 = 0
    scores = []
    score_table_1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score_table_2 = {')': 1, ']': 2, '}': 3, '>': 4}

    for entry in entry_list:
        stack = []
        corrupted = False
        auto_completion = ""
        for c in entry:
            if c in lefty:
                stack.append(c)
            elif c in righty:
                if righty.index(c) != lefty.index(stack.pop()):
                    score_1 += score_table_1[c]
                    corrupted = True
                    break
        if not corrupted:
            score_2 = 0
            # legal_entries.append(entry)
            if len(stack) != 0:
                for _ in range(len(stack)):
                    auto_completion += righty[lefty.index(stack.pop())]
            for c in auto_completion:
                score_2 *= 5
                score_2 += score_table_2[c]
            scores.append(score_2)

    scores = sorted(scores)
    middle_id = int(len(scores) / 2)
    score_2 = scores[middle_id]

    return score_1, score_2


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {syntax_checker(entries)[0]}')
print(f'Solution part 2: {syntax_checker(entries)[1]}')
