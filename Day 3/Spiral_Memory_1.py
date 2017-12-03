import sys
from enum import Enum
import math

class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 0

SPIRAL_MEMORY_LOCATION = int(sys.argv[1])

STEPS_OUT = 0

SIDE_LENGTH = 1

SPIRAL_CORNER_VALUE = 1
while SPIRAL_CORNER_VALUE < SPIRAL_MEMORY_LOCATION:
    # Add rows/columns to represent the spiral square growing
    SIDE_LENGTH += 2
    SPIRAL_CORNER_VALUE = SIDE_LENGTH * SIDE_LENGTH
    STEPS_OUT += 1

PREV_SIDE_LENGTH = SIDE_LENGTH - 2
PREV_SPIRAL_CORNER_VALUE = PREV_SIDE_LENGTH * PREV_SIDE_LENGTH
PREV_STEPS_OUT = STEPS_OUT - 1
print(f'The steps out of the spiral are {STEPS_OUT}')
print(f'Side length is saved as {SIDE_LENGTH}')

DIFFERENCE = SPIRAL_CORNER_VALUE - SPIRAL_MEMORY_LOCATION

print(f'Difference is {DIFFERENCE}')

SIDE = math.floor(DIFFERENCE/SIDE_LENGTH)

SPIRAL_ALONG_SIDE = DIFFERENCE % (SIDE_LENGTH - 1)

STEPS_ALONG_SIDE = SPIRAL_ALONG_SIDE

# In this case we're further back
if (STEPS_ALONG_SIDE > math.floor(SIDE_LENGTH / 2)):
    STEPS_ALONG_SIDE -= math.floor(SIDE_LENGTH / 2)
else: # elif (STEPS_ALONG_SIDE <= math.floor(SIDE_LENGTH / 2)):
    STEPS_ALONG_SIDE = math.floor(SIDE_LENGTH / 2) - STEPS_ALONG_SIDE

OUTPUT = STEPS_ALONG_SIDE + STEPS_OUT

print(f'Number of steps to reach this output in Spiral Memory is {OUTPUT}')