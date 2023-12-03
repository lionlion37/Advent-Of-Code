##########################################################
# Advent of Code 2020, Day Four: "Passport Processing"   #
# https://adventofcode.com/2020/day/4                    #
##########################################################

import os
import re

# get input ------------------------------------------------------------------------------------------------------------

# import puzzle input
with open(os.path.join('inputs', 'day4.txt'), 'r') as f:
    entry_list = f.readlines()

test_entry = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd', 'byr:1937 iyr:2017 cid:147 hgt:183cm', '\n',
              'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
              'hcl:#cfa07d byr:1929', '\n',
              'hcl:#ae17e1 iyr:2013',
              'eyr:2024',
              'ecl:brn pid:760753108 byr:1931',
              'hgt:179cm', '\n',
              'hcl:#cfa07d eyr:2025 pid:166559648',
              'iyr:2011 ecl:brn hgt:59in'
              ]

test_entry_invalid = ['eyr:1972 cid:100', 'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926', '\n',
                      'iyr:2019',
                      'hcl:#602927 eyr:1967 hgt:170cm',
                      'ecl:grn pid:012533040 byr:1946', '\n', 'hcl:dab227 iyr:2012',
                      'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277', '\n',
                      'hgt:59cm ecl:zzz',
                      'eyr:2038 hcl:74454a iyr:2023',
                      'pid:3556412378 byr:2007']

test_entry_valid = ['pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
                    'hcl:#623a2f', '\n',
                    'eyr:2029 ecl:blu cid:129 byr:1989',
                    'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm', '\n',
                    'hcl:#888785',
                    'hgt:164cm byr:2001 iyr:2015 cid:88',
                    'pid:545766238 ecl:hzl',
                    'eyr:2022', '\n',
                    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719']

# subfunction ----------------------------------------------------------------------------------------------------------


def validate(current_keys, optimal_keys):

    if current_keys == optimal_keys:
        return 1
    else:
        return 0


# function for part 1 and part 2 of the puzzle -------------------------------------------------------------------------


def check_passports(entries):
    """
    Checks a list of passport batches if all the expected fields (byr, iyr, eyr, hgt, hcl, ecl, pid) are present and
    return the number of passports with all required fields. Additionally, checks if the fields fulfill the required
    criteria (see AdventOfCode 2020, Day 4). :param entries: a list of passports where the passports are separated by
    one list entry '\n' :return: n_present: number of passports that have all required fields, n_valid: number of
    passports that have all required fileds which additionally fulfill the required criteria
    """
    keys = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
    keys_optimal = {'byr': True, 'iyr': True, 'eyr': True, 'hgt': True, 'hcl': True, 'ecl': True, 'pid': True}

    keys_temp_valid = keys.copy()
    keys_temp_present = keys.copy()
    n_valid = 0
    n_present = 0

    for line in entries:

        if 'byr' in line:

            keys_temp_present['byr'] = True
            n_present += validate(keys_temp_present, keys_optimal)

            pattern = 'byr:(\d*)'
            match = re.search(pattern, line)
            if match:
                try:
                    if 1920 <= int(match.group(1)) <= 2002:
                        keys_temp_valid['byr'] = True
                        n_valid += validate(keys_temp_valid, keys_optimal)
                except:
                    None

        if 'iyr' in line:

            keys_temp_present['iyr'] = True
            n_present += validate(keys_temp_present, keys_optimal)

            pattern = 'iyr:(\d*)'
            match = re.search(pattern, line)
            if match:
                try:
                    if 2010 <= int(match.group(1)) <= 2020:
                        keys_temp_valid['iyr'] = True
                        n_valid += validate(keys_temp_valid, keys_optimal)
                except:
                    None

        if 'eyr' in line:

            keys_temp_present['eyr'] = True
            n_present += validate(keys_temp_present, keys_optimal)

            pattern = 'eyr:(\d*)'
            match = re.search(pattern, line)
            if match:
                try:
                    if 2020 <= int(match.group(1)) <= 2030:
                        keys_temp_valid['eyr'] = True
                        n_valid += validate(keys_temp_valid, keys_optimal)
                except:
                    None

        if 'hgt' in line:

            keys_temp_present['hgt'] = True
            n_present += validate(keys_temp_present, keys_optimal)

            pattern = 'hgt:(\d*)([a-z]*)'
            match = re.search(pattern, line)
            try:
                if match:
                    if match.group(2) == 'cm':
                        if 150 <= int(match.group(1)) <= 193:
                            keys_temp_valid['hgt'] = True
                            n_valid += validate(keys_temp_valid, keys_optimal)
                    elif match.group(2) == 'in':
                        if 59 <= int(match.group(1)) <= 76:
                            keys_temp_valid['hgt'] = True
                            n_valid += validate(keys_temp_valid, keys_optimal)
            except:
                None

        if 'hcl' in line:

            keys_temp_present['hcl'] = True
            n_present += validate(keys_temp_present, keys_optimal)

            pattern = 'hcl:#([0-9a-f]*)'
            match = re.search(pattern, line)
            if match:
                if len(match.group(1)) == 6:
                    keys_temp_valid['hcl'] = True
                    n_valid += validate(keys_temp_valid, keys_optimal)

        if 'ecl' in line:

            keys_temp_present['ecl'] = True
            n_present += validate(keys_temp_present, keys_optimal)

            pattern = 'ecl:([a-z]*)'
            match = re.search(pattern, line)
            if match:
                if match.group(1) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    keys_temp_valid['ecl'] = True
                    n_valid += validate(keys_temp_valid, keys_optimal)

        if 'pid' in line:

            keys_temp_present['pid'] = True
            n_present += validate(keys_temp_present, keys_optimal)

            pattern = 'pid:(\d*)'
            match = re.search(pattern, line)
            if match:
                if len(match.group(1)) == 9:
                    keys_temp_valid['pid'] = True
                    n_valid += validate(keys_temp_valid, keys_optimal)

        if line == '\n':
            keys_temp_valid = keys.copy()
            keys_temp_present = keys.copy()

    return n_present, n_valid


# Solutions ------------------------------------------------------------------------------------------------------------

print(f'Solution part 1: {check_passports(entry_list)[0]}')
print(f'Solution part 2: {check_passports(entry_list)[1]}')
