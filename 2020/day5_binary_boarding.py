######################################################
# Advent of Code 2020, Day Five: "Binary Boarding"   #
# https://adventofcode.com/2020/day/5                #
######################################################

import os

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
with open(os.path.join('inputs', 'day5.txt'), 'r') as f:
    entry_list = f.readlines()

test_entry = ['BFFFBBFRRR\n', 'FFFBBBFRRR\n', 'BBFFBBFRLL\n']

# subfunction ----------------------------------------------------------------------------------------------------------


def characters(character, rows:list):
    if len(rows) > 2:
        if character == 'F' or character == 'L':
            return rows[0:int(len(rows)/2)]
        elif character == 'B' or character == 'R':
            return rows[(int(len(rows)/2)):int(len(rows))]

    if len(rows) == 2:
        if character == 'F' or character == 'L':
            return rows[0]
        elif character == 'B' or character == 'R':
            return rows[1]


# function for part 1 and part 2 of the puzzle -------------------------------------------------------------------------


def check_boarding_passes(entries):
    """
    Finds for a list of boarding passes the seat id, specified as row * 8 + column, for every boarding pass and returns
    the hightest seat id as well as the missing seat id in between all seats.
    :param entries: list of boarding passes of the form "XXXXXXXYYY" where X can either be "F" or "D", and Y can either
    be "R" or "L"
    :return: seat_id_max: highest seat id, missing_seat: missing seat id
    """
    seats = []
    seat_id_max = 0
    missing_seat = 0

    for boarding_pass in entries:
        boarding_pass = boarding_pass[:-1]
        row = list(range(128))
        column = list(range(8))

        for n, character in enumerate(boarding_pass):
            if n < 7:
                row = characters(character, row)
            else:
                column = characters(character, column)

        seat_id = row * 8 + column
        seats.append(seat_id)

        if seat_id > seat_id_max:
            seat_id_max = seat_id

    seats = sorted(seats)
    for seat in seats:
        if seat + 1 not in seats:
            missing_seat = seat + 1
            break

    return seat_id_max, missing_seat


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {check_boarding_passes(entry_list)[0]}')
print(f'Solution part 2: {check_boarding_passes(entry_list)[1]}')
