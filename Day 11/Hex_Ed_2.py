# Author Arthur Dooner
# Advent of Code Day 11
# Part 2
import math

MAX_X = 0
MAX_Y = 0
MAX_STEPS = 0

X_LOC = 0.0
Y_LOC = 0.0

def get_hexagonal_steps(X1, Y1):
    return abs(X1) * 2 + abs(Y1) - abs(X1)
# This was not the desired functionality, they wanted maximum hexagonal steps away
# def euclidean_distance_from_origin(X1, Y1):
#     return abs(X1) * 2 + abs(Y1) - abs(X1)

with open("Child_Process_Path.txt", "r") as inputLengths:
    for line in inputLengths:
        removedCommas = line.replace(',', ' ')
        elements = removedCommas.split()
        for element in elements:
            if element == 'n':
                Y_LOC += 1.0
            elif element == 'ne':
                X_LOC += .5
                Y_LOC += .5
            elif element == 'nw':
                X_LOC -= .5
                Y_LOC += .5
            elif element == 's':
                Y_LOC -= 1.0
            elif element == 'se':
                X_LOC += .5
                Y_LOC -= .5
            elif element == 'sw':
                X_LOC -= .5
                Y_LOC -= .5
            if get_hexagonal_steps(X_LOC, Y_LOC) > MAX_STEPS:
                MAX_X = X_LOC
                MAX_Y = Y_LOC
                MAX_EUCLIDEAN = get_hexagonal_steps(X_LOC, Y_LOC)

print(f'End Location X: {X_LOC} and Location Y: {Y_LOC}')

print(f'Steps that contributed to The Highest X and Y are {abs(MAX_X) * 2} and steps that contributed to just Y Steps are {abs(MAX_Y) - abs(MAX_X)}')

print(f'The minimum number of steps needed to reach the furthest away the child was (Part 2) are {abs(MAX_X) * 2 + abs(MAX_Y) - abs(MAX_X)}')