###################################################
# Advent of Code 2021, Day twenty: "Trench Map"   #
# https://adventofcode.com/2021/day/20            #
###################################################
    
import os
import numpy as np
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day20_custom.txt'), 'r') as f:
    entries = f.readlines()

algo = entries[0][:-1].replace('#', '1')
algo = algo.replace('.', '0')
img = []
for line in entries[2:]:
    l = line.replace('#', '1')
    l = l.replace('.', '0')
    img.append(list(l[:-1]))
img = np.array(img, dtype=int)

# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def process(algorithm, image, padding_value=0):
    output = np.zeros(shape=(image.shape[0]+2, image.shape[1]+2), dtype=int)
    image = np.pad(image, 2, mode='constant', constant_values=padding_value)

    for y in range(output.shape[0]):
        for x in range(output.shape[1]):
            square = image[y:y+3, x:x+3]
            idx = int(np.array2string(square.flatten(), separator="")[1:-1], 2)
            output[y, x] = int(algorithm[idx])

    return output


def enhance(algorithm, image, n_enhancements, visualize=False):
    for n in range(n_enhancements):
        if algorithm[0] == '1':
            padding_value = n % 2
        else:
            padding_value = 0
        image = process(algorithm, image, padding_value)

        if visualize:
            os.system('clear')
            for line in image:
                str_rep = np.array2string(line, separator='')[1:-1].replace('0', '.')
                str_rep = str_rep.replace('1', '#')
                str_rep = str_rep.replace('\n ', '')
                print(str_rep)

    return np.count_nonzero(image)


# Solutions ------------------------------------------------------------------------------------------------------------


# print(f'Solution part 1: {enhance(algo, img, 2)}')
print(f'Solution part 2: {enhance(algo, img, 63, True)}')
