import numpy as np


def get_neighbourhood(entries, y, x):
    """
    Gets adjacent neighbours (up, down, left, right, diagonals) of a specific element in 2d entry list.
    :param entries: 2d entry list that represents the current state of the waiting area
    :param y: y-value of seat for which the neighbourhood should be found
    :param x: x-value of seat for which the neighbourhood should be found
    :return: neighbourhood of given seat (including the seat itself)
    """
    if y == 0 and x != 0:
        neighbourhood = entries[y:y+2, x-1:x+2]
    elif y == 0 and x == 0:
        neighbourhood = entries[y:y+2, x:x+2]
    elif x == 0 and y != 0:
        neighbourhood = entries[y-1:y+2, x:x+2]
    elif y >= len(entries) - 1 and x < len(entries[0]) - 1:
        neighbourhood = entries[y-1:y+1, x-1:x+2]
    elif y >= len(entries) - 1 and x >= len(entries[0]) - 1:
        neighbourhood = entries[y-1:y+1, x-1:x+1]
    elif x >= len(entries[0]) - 1 and y < len(entries) - 1:
        neighbourhood = entries[y-1:y+2, x-1:x+1]
    else:
        neighbourhood = entries[y-1:y+2, x-1:x+2]

    return neighbourhood


def get_sight(entries, y, x):
    """
    Searches in each direction from a specific seat for what can be seen first: a occupied or free seat or no seat.
    :param entries: 2d entry list that represents the current state of the waiting area
    :param y: y-value of seat for which the neighbourhood should be found
    :param x: x-value of seat for which the neighbourhood should be found
    :return: for each direction what can be seen first
    """
    diagonal_up_left = -1
    y_dul = y - 1
    x_dul = x - 1
    while y_dul >= 0 and x_dul >= 0:
        if entries[y_dul, x_dul] == 0:
            diagonal_up_left = 0
            break
        elif entries[y_dul, x_dul] == 1:
            diagonal_up_left = 1
            break
        y_dul -= 1
        x_dul -= 1

    diagonal_up_right = -1
    y_dur = y - 1
    x_dur = x + 1
    while y_dur >= 0 and x_dur < len(entries[0]):
        if entries[y_dur, x_dur] == 0:
            diagonal_up_right = 0
            break
        elif entries[y_dur, x_dur] == 1:
            diagonal_up_right = 1
            break
        y_dur -= 1
        x_dur += 1

    diagonal_down_left = -1
    y_ddl = y + 1
    x_ddl = x - 1
    while y_ddl < len(entries) and x_ddl >= 0:
        if entries[y_ddl, x_ddl] == 0:
            diagonal_down_left = 0
            break
        elif entries[y_ddl, x_ddl] == 1:
            diagonal_down_left = 1
            break
        y_ddl += 1
        x_ddl -= 1

    diagonal_down_right = -1
    y_ddr = y + 1
    x_ddr = x + 1
    while y_ddr < len(entries) and x_ddr < len(entries[0]):
        if entries[y_ddr, x_ddr] == 0:
            diagonal_down_right = 0
            break
        elif entries[y_ddr, x_ddr] == 1:
            diagonal_down_right = 1
            break
        y_ddr += 1
        x_ddr += 1

    up = -1
    y_u = y - 1
    while y_u >= 0:
        if entries[y_u, x] == 0:
            up = 0
            break
        elif entries[y_u, x] == 1:
            up = 1
            break
        y_u -= 1

    down = -1
    y_d = y + 1
    while y_d < len(entries):
        if entries[y_d, x] == 0:
            down = 0
            break
        elif entries[y_d, x] == 1:
            down = 1
            break
        y_d += 1

    left = -1
    x_l = x - 1
    while x_l >= 0:
        if entries[y, x_l] == 0:
            left = 0
            break
        elif entries[y, x_l] == 1:
            left = 1
            break
        x_l -= 1

    right = -1
    x_r = x + 1
    while x_r < len(entries[0]):
        if entries[y, x_r] == 0:
            right = 0
            break
        elif entries[y, x_r] == 1:
            right = 1
            break
        x_r += 1

    return left, diagonal_up_left, up, diagonal_up_right, right, diagonal_down_right, down, diagonal_down_left


def simulate_seats(entries, part):
    """
    Simulates the next state of the waiting area based on a given set of rules.
    :param entries: 2d entry list that represents the current state of the waiting area
    :param part: select set of rules by setting this to either 1 (rules of part 1) or 2 (rules of part 2)
    :return: the next state
    """
    next_stage = entries.copy()

    if part == 1:
        for y, row in enumerate(entries):
            for x, seat in enumerate(row):
                if seat == -1:
                    continue
                elif seat == 0:
                    neighbourhood = get_neighbourhood(entries, y, x)
                    if 1 not in neighbourhood:
                        next_stage[y, x] = 1
                elif seat == 1:
                    neighbourhood = get_neighbourhood(entries, y, x)
                    n_occ = np.count_nonzero(neighbourhood == 1) - 1
                    if n_occ >= 4:
                        next_stage[y, x] = 0

    elif part == 2:
        for y, row in enumerate(entries):
            for x, seat in enumerate(row):
                if seat == -1:
                    continue
                elif seat == 0:
                    neighbourhood = list(get_sight(entries, y, x))
                    if 1 not in neighbourhood:
                        next_stage[y, x] = 1
                elif seat == 1:
                    neighbourhood = list(get_sight(entries, y, x))
                    n_occ = neighbourhood.count(1)
                    if n_occ >= 5:
                        next_stage[y, x] = 0
    return next_stage
