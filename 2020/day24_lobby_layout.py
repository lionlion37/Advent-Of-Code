#########################################################
# Advent of Code 2020, Day Twentyfour: "Lobby Layout"   #
# https://adventofcode.com/2020/day/24                  #
#########################################################

import os
import numpy as np

# get input ------------------------------------------------------------------------------------------------------------

with open(os.path.join('inputs', 'day24.txt'), 'r') as f:
    entry_list = []
    for line in f.readlines():
        entry_list.append(line[:-1])

test = ['sesenwnenenewseeswwswswwnenewsewsw',
        'neeenesenwnwwswnenewnwwsewnenwseswesw',
        'seswneswswsenwwnwse',
        'nwnwneseeswswnenewneswwnewseswneseene',
        'swweswneswnenwsewnwneneseenw',
        'eesenwseswswnenwswnwnwsewwnwsene',
        'sewnenenenesenwsewnenwwwse',
        'wenwwweseeeweswwwnwwe',
        'wsweesenenewnwwnwsenewsenwwsesesenwne',
        'neeswseenwwswnwswswnw',
        'nenwswwsewswnenenewsenwsenwnesesenew',
        'enewnwewneswsewnwswenweswnenwsenwsw',
        'sweneswneswneneenwnewenewwneswswnese',
        'swwesenesewenwneswnwwneseswwne',
        'enesenwswwswneneswsenwnewswseenwsese',
        'wnwnesenesenenwwnenwsewesewsesesew',
        'nenewswnwewswnenesenwnesewesw',
        'eneswnwswnwsenenwnwnwwseeswneewsenese',
        'neswnwewnwnwseenwseesewsenwsweewe',
        'wseweeenwnesenwwwswnew']


# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entries):                                     # y is  odd    even
    instruction_catalog = {'e': [1, 0], 'w': [-1, 0], 'se': [[0, 1], [1, 1]], 'ne': [[0, -1], [1, -1]],
                           'sw': [[-1, 1], [0, 1]], 'nw': [[-1, -1], [0, -1]]}
    coordinate_system = {'[0 0]': False}

    for instruction in entries:
        current_point = np.array([0, 0])
        n = 0
        while n < len(instruction):
            direction = instruction[n]
            if direction in ['n', 's']:
                direction = instruction[n:n+2]
                if current_point[1] % 2 == 0:
                    o_e_id = 1
                else:
                    o_e_id = 0
                current_point += np.array(instruction_catalog[direction][o_e_id])
                n += 2
            else:
                current_point += np.array(instruction_catalog[direction])
                n += 1
        if str(current_point) in coordinate_system.keys():
            coordinate_system[str(current_point)] = not coordinate_system[str(current_point)]
        else:
            coordinate_system[str(current_point)] = True

        if str(current_point) not in coordinate_system:
            sign_x, sign_y = False, False
            current_x = abs(current_point[0])
            current_y = abs(current_point[1])
            if current_point[0] < 0:
                sign_x = True
            if current_point[1] < 0:
                sign_y = True
            for x in range(current_x):
                for y in range(current_y):
                    if sign_x:
                        x *= -1
                    if sign_y:
                        y *= -1
                    if f'[{x}, {y}]' not in coordinate_system:
                        coordinate_system[f'[{x}, {y}]'] = False

    return coordinate_system


# Solutions ------------------------------------------------------------------------------------------------------------

c_s = part1(test)

black = 0
for el in c_s:
    if c_s[el]:
        black += 1

print(black, c_s)
