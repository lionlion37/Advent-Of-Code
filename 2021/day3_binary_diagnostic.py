#########################################################
# Advent of Code 2021, Day three: "Binary Diagnostic"   #
# https://adventofcode.com/2021/day/3                   #
#########################################################
    
import os
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day3.txt'), 'r') as f:
    entries = f.readlines()
    entries = np.array([[int(bit) for bit in entry[:-1]] for entry in entries])
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def diagnose(entry_list):
    n_zero, n_one = [], []
    oxygen, co2 = entry_list.copy(), entry_list.copy()

    for col in range(len(entry_list[0])):
        # part 1
        count = np.bincount(entry_list[:, col])
        n_zero.append(count[0])
        n_one.append(count[1])

        # part 2
        count_oxygen, count_co2 = np.bincount(oxygen[:, col]), np.bincount(co2[:, col])

        if len(oxygen) > 1:
            oxygen = oxygen[np.where(oxygen[:, col] == int(count_oxygen[0] <= count_oxygen[1]))]
        if len(co2) > 1:
            co2 = co2[np.where(co2[:, col] == int(count_co2[0] > count_co2[1]))]

    n_zero, n_one = np.array(n_zero), np.array(n_one)
    gamma, epsilon = np.array(n_one > n_zero) * 1, np.array(n_one < n_zero) * 1

    # convert numpy arrays to strings
    gamma, epsilon, oxygen, co2 = "".join(gamma.astype(str)), "".join(epsilon.astype(str)), \
                                  "".join(oxygen[0].astype(str)), "".join(co2[0].astype(str))

    return int(gamma, 2) * int(epsilon, 2), int(oxygen, 2) * int(co2, 2)


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {diagnose(entries)[0]}')
print(f'Solution part 2: {diagnose(entries)[1]}')
