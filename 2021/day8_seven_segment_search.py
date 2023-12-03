############################################################
# Advent of Code 2021, Day eight: "Seven Segment Search"   #
# https://adventofcode.com/2021/day/8                      #
############################################################
    
import os
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day8.txt'), 'r') as f:
    entries = f.readlines()

out = []
inp = []

for n, sig in enumerate(entries):
    sig_list = sig[:-1].split(' ')
    out.append(sig_list[11:])
    inp.append(sig_list[:10])
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def part1(outputs):
    n_unique = 0
    for signal in outputs:
        for digit in signal:
            if len(digit) in [2, 3, 4, 7]:
                n_unique += 1

    return n_unique


def part2(inputs, outputs):

    result = 0

    for inp, out in zip(inputs, outputs):

        representations = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

        # get representations of digits with unique segment length
        for digit in inp:
            digit = "".join(sorted(digit))
            if len(digit) == 7:
                representations[8] = digit
            elif len(digit) == 4:
                representations[4] = digit
            elif len(digit) == 3:
                representations[7] = digit
            elif len(digit) == 2:
                representations[1] = digit
            if representations[1] and representations[4] and representations[7] and representations[8]:
                break

        # get representation of digits with segment length 6 and segment length 5
        for digit in inp:
            digit = "".join(sorted(digit))

            if len(digit) == 6 and (not representations[6] or not representations[0] or not representations[9]):
                if add_str(digit, representations[1]) == representations[8]:
                    representations[6] = digit
                elif len(substract_str(representations[4], digit)) == 1:
                    representations[0] = digit
                else:
                    representations[9] = digit

            if len(digit) == 5 and (not representations[2] or not representations[3] or not representations[5]):
                if add_str(digit, representations[4]) == representations[8]:
                    representations[2] = digit
                elif len(substract_str(representations[7], digit)) == 1:
                    representations[5] = digit
                else:
                    representations[3] = digit

        decoded = ""
        for digit in out:
            digit = "".join(sorted(digit))
            for rep in representations.keys():
                if representations[rep] == digit:
                    decoded += str(rep)
                    break

        result += int(decoded)

    return result


def add_str(str1, str2):
    for s in str2:
        if not (s in str1):
            str1 += s
    return "".join(sorted(str1))


def substract_str(str1, str2):
    result = ""
    for s in str1:
        if not (s in str2):
            result += s
    return "".join(sorted(result))


# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(out)}')
print(f'Solution part 2: {part2(inp, out)}')
