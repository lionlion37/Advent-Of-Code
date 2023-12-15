######################################################
# Advent of Code 2023, Day fifteen: "lens library"   #
# https://adventofcode.com/2023/day/15               #
######################################################
    
import os
import re
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day15.txt'), 'r') as f:
    entries = f.read()
    input_strings = entries.strip().split(',')
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def hash_string(string):
    current_hash = 0
    for char in string:
        current_hash += ord(char)
        current_hash *= 17
        current_hash = current_hash % 256
    return current_hash


def part1(strings):
    result = 0
    for string in strings:
        result += hash_string(string)

    return result


def part2(strings):
    label_pat = r'[a-zA-Z]+'
    operation_pat = r'[\-=]'
    boxes = [0] * 256
    result = 0

    for string in strings:
        label = re.search(label_pat, string).group()
        operation = re.search(operation_pat, string).group()
        box_idx = hash_string(label)
        current_box = np.array(boxes[box_idx])

        if operation == '=':  # add lens
            focal_len = string[-1]
            if current_box == 0:  # no lenses in box
                new_box = [[label, focal_len]]
                boxes[box_idx] = new_box

            else:  # lenses in box
                if np.any(current_box[:, 0] == label):  # label already present
                    lens_idx = np.where(current_box[:, 0] == label)[0]
                    current_box[lens_idx, 1] = focal_len
                    boxes[box_idx] = current_box.tolist()
                else:  # label not present
                    current_box = current_box.tolist()
                    current_box.insert(0, [label, focal_len])
                    boxes[box_idx] = current_box

        else:  # remove lens
            if current_box == 0:
                continue
            if np.any(current_box[:, 0] == label):  # label present
                if len(current_box) == 1:  # remove last lens in box
                    boxes[box_idx] = 0
                    continue
                lens_idx = int(np.where(current_box[:, 0] == label)[0])
                current_box = current_box.tolist()
                current_box = current_box[:lens_idx] + current_box[lens_idx + 1:]
                boxes[box_idx] = current_box
            else:  # label not present, nothing to remove
                continue

    for box_idx, box in enumerate(boxes):
        if box == 0:
            continue
        for slot_num, lens in enumerate(box):
            focusing_power = (box_idx + 1) * (len(box) - slot_num) * int(lens[1])
            result += focusing_power

    return result


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {part1(input_strings)}')
print(f'Solution part 2: {part2(input_strings)}')
