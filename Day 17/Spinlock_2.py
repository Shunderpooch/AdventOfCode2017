import sys

NUMBER_STEPS = None
NUMBER_INSERTIONS = 50000001
CURRENT_INSERTION = 1
CURRENT_INDEX = 0
LIST_LEN = 1

if len(sys.argv) != 2:
    print(f'Invalid input! Please write your key string after the program name.')
    exit(0)

NUMBER_STEPS = int(sys.argv[1]) # My puzzle input was '370'
RESULT = None
# Intuitively we know the first element has elements around it, and more end up between 
while CURRENT_INSERTION < NUMBER_INSERTIONS: # As long as we're lower than the insertion
    CURRENT_INDEX += NUMBER_STEPS # Index incremented from 
    TEMP_POS = CURRENT_INDEX % LIST_LEN # Get the value within bounds
    if TEMP_POS == 0: # If we're at the necessary state of 0
        RESULT = CURRENT_INSERTION # Track the insertion
    LIST_LEN += 1 # Increment the size of the list
    CURRENT_INDEX = TEMP_POS + 1 # Generate the index from the value we want + 1
    CURRENT_INSERTION += 1 # Count up

print(f'The number that occurs directly after 0 in the generated list (Part 2) is {RESULT}')