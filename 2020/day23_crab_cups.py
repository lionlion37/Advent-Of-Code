#######################################################
# Advent of Code 2020, Day Twentythree: "Crab Cups"   #
# https://adventofcode.com/2020/day/23                #
#######################################################
    
# get input ------------------------------------------------------------------------------------------------------------

current_id = 0
entry = [int(n) for n in str(614752839)]
test = [int(n) for n in str(389125467)]
    
# functions for part 1 and part 2 of the puzzle ------------------------------------------------------------------------


def one_step(current_state, current_id):
    current_cup = current_state[current_id]
    if current_id + 4 <= len(current_state):
        pick_up = current_state[current_cup:current_state+4]

    found = False
    destination_cup = int(current_cup) - 1
    while not found:
        if destination_cup not in pick_up:
            found = True
        else:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = max(entry.split(''))





# Solutions ------------------------------------------------------------------------------------------------------------
