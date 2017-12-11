import sys
from enum import Enum
import math

class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 0

SIDE_LENGTH = 3
 
def get_next_direction(aDirection, aLocation):
    global SIDE_LENGTH
    half_side_length = math.floor(SIDE_LENGTH/2)
    if aDirection == Direction.DOWN and aLocation[1] * -1 == half_side_length:
        return Direction.RIGHT
    elif aDirection == Direction.RIGHT and aLocation[0] == half_side_length + 1: #Special case for spiral
        SIDE_LENGTH += 2
        return Direction.UP
    elif aDirection == Direction.UP and aLocation[1] == half_side_length: 
        return Direction.LEFT
    elif aDirection == Direction.LEFT and aLocation[0] * -1 == half_side_length:
        return Direction.DOWN
    else :
        return aDirection

def get_next_location(aLocation, aDirection):
    if aDirection == Direction.DOWN:
        newLocation = tuple(map(sum, zip(aLocation, (0, -1))))
        return newLocation
    elif aDirection == Direction.RIGHT:
        newLocation = tuple(map(sum, zip(aLocation, (1, 0))))
        return newLocation
    elif aDirection == Direction.UP:
        newLocation = tuple(map(sum, zip(aLocation, (0, 1))))
        return newLocation
    else:
        newLocation = tuple(map(sum, zip(aLocation, (-1, 0))))
        return newLocation

SPIRAL_MEMORY_LOCATION = int(sys.argv[1])

STEPS_OUT = 0
SPIRAL_VALUE = 1
# DICT GOES [x, y]
SPIRAL_MEMORY_AS_DICT = {(0, 0): 1} 

def get_all_neighbors(inputLoc):
    global SPIRAL_MEMORY_AS_DICT
    active_neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            tempTuple = tuple(map(sum, zip(inputLoc, (i, j))))
            # print (f'Potential Neighbor at {tempTuple}')
            if (tempTuple in SPIRAL_MEMORY_AS_DICT.keys()):
                # print (f'Active Neighbor at {tempTuple}')
                active_neighbors.append(tempTuple)
    return active_neighbors

def get_sum_neighbors(neighbors):
    global SPIRAL_MEMORY_AS_DICT
    resultSum = 0
    for neighbor in neighbors:
        resultSum += SPIRAL_MEMORY_AS_DICT[neighbor]
    return resultSum

current_x = 1
current_y = 0
current_direction = Direction.UP
# ITERATION_NUM = 0
while SPIRAL_VALUE < SPIRAL_MEMORY_LOCATION:
    # ITERATION_NUM += 1
    # print(f'Iteration {ITERATION_NUM}:')
    neighbors = get_all_neighbors((current_x, current_y))
    SPIRAL_VALUE = get_sum_neighbors(neighbors)
    SPIRAL_MEMORY_AS_DICT.update({(current_x, current_y): SPIRAL_VALUE})
    current_direction = get_next_direction(current_direction, (current_x, current_y))
    next_location = get_next_location((current_x, current_y), current_direction)
    current_x = next_location[0]
    current_y = next_location[1]
    # if (SPIRAL_VALUE != 0) :
    #     print(f'{SPIRAL_VALUE}')
    #     print(f'{current_direction}')
    #     print(f'{next_location}')


print(f'For Part 2: The first value written that is larger than my puzzle input is {SPIRAL_VALUE}')