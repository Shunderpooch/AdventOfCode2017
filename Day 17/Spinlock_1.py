import sys

NUMBER_STEPS = None
NUMBER_INSERTIONS = 2018 # One more than the specified 2017 for 2017 inclusive
CURRENT_INSERTION = 1
CURRENT_INDEX = 0
SAVED_LIST = [0] # List Initial State

if len(sys.argv) != 2:
    print(f'Invalid input! Please write your key string after the program name.')
    exit(0)

NUMBER_STEPS = int(sys.argv[1]) # My puzzle input was '370'

while CURRENT_INSERTION < NUMBER_INSERTIONS:
    for step in range(0, NUMBER_STEPS):
        CURRENT_INDEX += 1
        if CURRENT_INDEX == len(SAVED_LIST):
            CURRENT_INDEX = 0
    SAVED_LIST.insert(CURRENT_INDEX + 1, CURRENT_INSERTION)
    CURRENT_INDEX = CURRENT_INDEX + 1
    #print(SAVED_LIST)

    CURRENT_INSERTION += 1

INSERTION_INDEX = SAVED_LIST.index((NUMBER_INSERTIONS - 1))
print(f'The number that occurs directly after {NUMBER_INSERTIONS - 1} in the generated list (Part 1) is {SAVED_LIST[INSERTION_INDEX + 1]}')