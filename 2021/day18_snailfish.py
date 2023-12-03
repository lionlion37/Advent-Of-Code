####################################################
# Advent of Code 2021, Day eighteen: "Snailfish"   #
# https://adventofcode.com/2021/day/18             #
####################################################
    
import os
import ast  # literal_eval
    
# get input ------------------------------------------------------------------------------------------------------------
    
with open(os.path.join('inputs', 'day18_test.txt'), 'r') as f:
    entries = f.readlines()
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


class Element:
    def __init__(self, element, depth):
        self.depth = depth
        self.parent = None
        if type(element[0]) == int and type(element[1]) == int:
            self.element_1 = element[0]
            self.element_2 = element[1]

        elif type(element[0]) == int and type(element[1]) == list:
            self.element_1 = element[0]
            self.element_2 = Element(element[1], self.depth + 1)
            self.element_2.parent = self

        elif type(element[0]) == list and type(element[1]) == int:
            self.element_1 = Element(element[0], self.depth + 1)
            self.element_1.parent = self
            self.element_2 = element[1]

        else:
            self.element_1 = Element(element[0], self.depth + 1)
            self.element_1 = self
            self.element_2 = Element(element[1], self.depth + 1)
            self.element_2 = self

    def get_depth(self):
        return self.depth

    def to_list(self):
        result = []
        if type(self.element_1) == Element:
            result.append(self.element_1.to_list())
        else:
            result.append(self.element_1)
        if type(self.element_2) == Element:
            result.append(self.element_2.to_list())
        else:
            result.append(self.element_2)

        return result

    def add_list(self, element):
        self.element_1 = Element(self.to_list(), 1)
        if type(element) == list:
            self.element_2 = Element(element, 1)
        else:
            self.element_2 = element

    def find_left(self):
        # Returns the regular number node to the left of this snailfish node
        current = self
        parent = self.parent

        left = None
        while True:
            if parent == None:
                return None
            left = parent.element_1
            if type(left) == int:
                # bob's your uncle
                return left
            if left is not current:
                break
            current = parent
            parent = parent.parent

        if left == None:
            # this node has the left-most item
            return None

        # find the right-most item in the left tree
        while not type(left.element_2) == int:
            left = left.element_2
        return left.element_2



def part1(entry_list):
    current_number = entry_list[0]

    
    
def part2(entry_list):
    pass

# Solutions ------------------------------------------------------------------------------------------------------------


el = Element([[[[1,2],[3,4]],[[5,6],[7,8]]],9], 0)
d
# print(f'Solution part 1: {part1(entries)}')
# print(f'Solution part 2: {part2(entries)}')
