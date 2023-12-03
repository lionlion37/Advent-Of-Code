#########################################################
# Advent of Code 2020, Day Thirteen: "Shuttle Search"   #
# https://adventofcode.com/2020/day/13                  #
#########################################################
    
import os
import re
import numpy as np

# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day13.txt'), 'r') as f:
    entry_list = f.readlines()

test_entry_1 = ['939\n', '7,13,x,x,59,x,31,19']  # 1068781
test_entry_2 = ['', '67,7,59,61']  # 754018
test_entry_3 = ['', '67,x,7,59,61']  # 779210
test_entry_4 = ['', '67,7,x,59,61']  # 1261476
test_entry_5 = ['', '1789,37,47,1889']  # 1202161486
test_entry_6 = ['', '17,x,13,19']  # 3417

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(entries):
    earliest_depature = int(entries[0])
    bus_ids = entries[1]
    bus_available = re.findall('\d+', bus_ids)
    depature_times = []

    for bus in bus_available:
        depature_times.append(int(earliest_depature / int(bus)) * int(bus) + int(bus))

    waiting_time = min(depature_times) - earliest_depature
    bus_id_ideal = int(bus_available[depature_times.index(min(depature_times))])

    return waiting_time * bus_id_ideal


def valid_7_13(n):
    return 7 * (11 + 13 * (n-1))


def part2(entries, ts=False):
    bus_ids = re.findall('\d+|x+', entries[1])
    for n, i in enumerate(bus_ids):
        if i != 'x':
            bus_ids[n] = int(i)

    results = []
    i1 = bus_ids[0]

    for t, i2 in enumerate(bus_ids):
        if i2 == 'x' or i1 == i2:
            continue
        r1 = i1
        r2 = i2
        while r2 - r1 != t:
            while r2 - r1 > t:
                r1 += i1
                if r2 - r1 == t:
                    break
            if r2 - r1 < t:
                r2 += i2

        results.append([r1 / i1, i2])

    results = np.array(results)
    ts = 100000000000000
    if ts:
        for n, r in enumerate(results):
            ca = int((int(ts / i1) - r[0]) / r[1])
            results[n][0] = r[0] + r[1] * ca
    found = False
    while not found:
        m = max(results[:, 0])
        for n, el in enumerate(results[:, 0]):
            while el < m:
                el += results[n, 1]
            results[n, 0] = el
            to_print = el * i1
            os.system('clear')
            print(to_print)
        if np.all(results[:, 0] == results[0, 0]):
            found = True

    return results[0, 0] * i1


# Solutions ------------------------------------------------------------------------------------------------------------

# print(f'Solution part 1: {part1(entry_list)}')
print(part2(entry_list, True))
# print(valid_7_13(4))
