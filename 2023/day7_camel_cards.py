###################################################
# Advent of Code 2023, Day seven: "camel cards"   #
# https://adventofcode.com/2023/day/7             #
###################################################
    
import os
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day7.txt'), 'r') as f:
    inp_hands = []
    for entry in f.readlines():
        hand, bid = entry.split()
        inp_hands.append([hand, bid])
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------

conversion_1 = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
conversion_2 = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}


def to_hex(hand, part):
    if part == 1:
        conversion = conversion_1
    else:
        conversion = conversion_2
    hand = hand[0]
    result = '0x'
    for char in hand:
        try:
            int_char = int(char)
            result += str(hex(int_char))[-1]
        except ValueError:
            converted_char = conversion[char]
            result += str(hex(converted_char))[-1]
    return result


def get_joker_type(hand):
    highest_type = 6
    cards = hand[0]
    for card in ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
        current_type = get_hand_type([cards.replace('J', card), hand[1]], 2)
        if current_type < highest_type:
            highest_type = current_type
    return highest_type


def get_hand_type(hand, part):
    """
    0 = five of a kind
    1 = four of a kind
    2 = full house
    3 = three of a kind
    4 = two pair
    5 = one pair
    6 = high card
    """
    cards = hand[0]
    if part == 2:
        if 'J' in cards:
            return get_joker_type(hand)
    if len(set(cards)) == 1:  # five of a kind
        return 0
    elif len(set(cards)) == len(cards):  # high card
        return 6
    elif len(set(cards)) == len(cards) - 1:  # one pair
        return 5
    elif len(set(cards)) == 2:
        c = cards.count(list(set(cards))[0])
        if c == 4 or c == 1:  # four of a kind
            return 1
        else:
            return 2  # full house
    else:
        c1 = cards.count(list(set(cards))[0])
        c2 = cards.count(list(set(cards))[1])
        c3 = cards.count(list(set(cards))[2])
        if 3 in [c1, c2, c3]:  # three of a kind
            return 3
        else:  # two pairs
            return 4


def part1(hands, part):
    hands_grouped = np.array([get_hand_type(hand, part) for hand in hands])
    hands_sorted = []
    for g in [6, 5, 4, 3, 2, 1, 0]:
        if g in hands_grouped:
            g_idx = np.where(hands_grouped == g)[0]
            hands_sorted += sorted([[to_hex(hand, part), hand[1]] for hand in np.array(hands)[g_idx]])

    ordered_bids = np.array([int(hand[1]) for hand in hands_sorted])
    result = ordered_bids @ np.arange(1, len(ordered_bids) + 1)

    return result


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(inp_hands, 1)}')
print(f'Solution part 2: {part1(inp_hands, 2)}')
