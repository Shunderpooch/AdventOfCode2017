# Author Arthur Dooner
# Advent of Code Day 15
# Part 1, "Dueling Generators"

import sys


FACTORS = [16807, 48271] # Generator A and B factors respectively
CURRENT_VALUES = [] # Index 0 for A, 1 for B
NUM_ITERATIONS = 40000000

with open("Generator_States.txt", "r") as states:
    for a_state in states:
        elements = a_state.split()
        CURRENT_VALUES.append(int(elements[len(elements) - 1]))

def run_iteration(factors, values):
    counter = 0
    while counter < len(values):
        values[counter] = (values[counter] * factors[counter]) % 2147483647
        counter += 1

def check_values(values):
    return "{0:b}".format(values[0])[-16:] == "{0:b}".format(values[1])[-16:]

CURRENT_ITERATION = 0
SCORE = 0
while CURRENT_ITERATION < NUM_ITERATIONS:
    run_iteration(FACTORS, CURRENT_VALUES)
    if check_values(CURRENT_VALUES):
        SCORE += 1
    CURRENT_ITERATION += 1

print(f'The number of times the lowest 16 bits were equivalent in Generators A and B in {NUM_ITERATIONS} was {SCORE}')