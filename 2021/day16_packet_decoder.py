########################################################
# Advent of Code 2021, Day sixteen: "Packet Decoder"   #
# https://adventofcode.com/2021/day/16                 #
########################################################
    
import os
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day16.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def hex_to_binary(number):
    output = ""
    hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    for n in number:
        output += hex_dict[n]
    return output


def get_packet(transmission):

    type_id = int(transmission[3:6], 2)

    if type_id == 4:  # Literal packet
        return LiteralPacket(transmission)
    else:  # Operator packet
        return OperatorPacket(transmission)


class LiteralPacket:
    def __init__(self, entry_list):
        self.binary = entry_list
        self.version = int(self.binary[:3], 2)
        self.type_id = int(self.binary[3:6], 2)
        self.len = 6

        self.number = ""
        bin_value = self.binary[6:]

        # Calculate literal value
        last_group = False
        for n in range(0, len(bin_value), 5):
            if last_group:
                break
            current_num = bin_value[n:n+5]
            last_group = not bool(int(current_num[0]))
            self.len += 5
            self.number += current_num[1:]

    def __len__(self):
        return self.len


class OperatorPacket:
    def __init__(self, entry_list):
        self.binary = entry_list
        self.version = int(self.binary[:3], 2)
        self.type_id = int(self.binary[3:6], 2)
        self.len = 7
        self.children = []

        self.length_type_id = int(self.binary[6])

        # Length Type ID 0: length of operator is defined by fixed bit number
        if self.length_type_id == 0:
            len_sub_packets = int(self.binary[7:22], 2)
            self.len += len_sub_packets + 15
            remaining_len = 0
            self.argument = self.binary[22:22+len_sub_packets]

            while True:
                current_child = get_packet(self.argument[remaining_len:])
                remaining_len += len(current_child)
                self.children.append(current_child)
                if remaining_len == len_sub_packets:
                    break

        # Length Type ID 1: length of operator is defined by number of sub-packets
        else:
            self.len += 11
            n_sub_packets = int(self.binary[7:18], 2)
            current_idx = 0
            self.argument = self.binary[18:]

            for _ in range(n_sub_packets):
                current_child = get_packet(self.argument[current_idx:])
                current_idx += len(current_child)
                self.len += len(current_child)
                self.children.append(current_child)

    def __len__(self):
        return self.len


def count_version(packet):

    if type(packet) == LiteralPacket:
        return packet.version

    else:
        total_version = packet.version
        for child in packet.children:
            total_version += count_version(child)
        return total_version


def calculate_tree(packet):
    if type(packet) == LiteralPacket:
        return int(packet.number, 2)

    # sum
    elif packet.type_id == 0:
        result = 0
        for child in packet.children:
            result += calculate_tree(child)
    # product
    elif packet.type_id == 1:
        result = 1
        for child in packet.children:
            result *= calculate_tree(child)
    # min
    elif packet.type_id == 2:
        result = float('inf')
        for child in packet.children:
            current_val = calculate_tree(child)
            if current_val < result:
                result = current_val
    # max
    elif packet.type_id == 3:
        result = float('-inf')
        for child in packet.children:
            current_val = calculate_tree(child)
            if current_val > result:
                result = current_val
    # larger than
    elif packet.type_id == 5:
        if calculate_tree(packet.children[0]) > calculate_tree(packet.children[1]):
            result = 1
        else:
            result = 0
    # less than
    elif packet.type_id == 6:
        if calculate_tree(packet.children[0]) < calculate_tree(packet.children[1]):
            result = 1
        else:
            result = 0
    # equal
    elif packet.type_id == 7:
        if calculate_tree(packet.children[0]) == calculate_tree(packet.children[1]):
            result = 1
        else:
            result = 0

    return result


def part1(entry_list):
    p = OperatorPacket(hex_to_binary(entry_list[0][:-1]))
    return count_version(p)


def part2(entry_list):
    p = OperatorPacket(hex_to_binary(entry_list[0][:-1]))
    return calculate_tree(p)

# Solutions ------------------------------------------------------------------------------------------------------------


print(f'Solution part 1: {part1(entries)}')
print(f'Solution part 2: {part2(entries)}')
