# Author Arthur Dooner
# Advent of Code Day 11
# Part 1

STEPS_DICT = {}

with open("Child_Process_Path.txt", "r") as inputLengths:
    for line in inputLengths:
        removedCommas = line.replace(',', ' ')
        elements = removedCommas.split()
        for element in elements:
            if element in STEPS_DICT:
                STEPS_DICT[element] += 1
            else:
                STEPS_DICT[element] = 1


X_LOC = 0
Y_LOC = 0
if 'n' in STEPS_DICT:
    Y_LOC += STEPS_DICT['n']

if 'ne' in STEPS_DICT:
    X_LOC += STEPS_DICT['ne']/2
    Y_LOC += STEPS_DICT['ne']/2

if 'nw' in STEPS_DICT:
    X_LOC -= STEPS_DICT['nw']/2
    Y_LOC += STEPS_DICT['nw']/2

if 's' in STEPS_DICT:
    Y_LOC -= STEPS_DICT['s']

if 'se' in STEPS_DICT:
    X_LOC += STEPS_DICT['se']/2
    Y_LOC -= STEPS_DICT['se']/2

if 'sw' in STEPS_DICT:
    X_LOC -= STEPS_DICT['sw']/2
    Y_LOC -= STEPS_DICT['sw']/2

print(f'Location X: {X_LOC} and Location Y: {Y_LOC}')

print(f'Steps that contributed to X and Y are {abs(X_LOC) * 2} and steps that contributed to just Y Steps are {abs(Y_LOC) - abs(X_LOC)}')

print(f'The minimum number of steps needed to reach the child (Part 1) are {abs(X_LOC) * 2 + abs(Y_LOC) - abs(X_LOC)}')