# Author Arthur Dooner
# Advent of Code Day 13
# Part 2
import math

MAX_DEPTH = 0
PICOSECOND_COUNTER = 0
CURRENT_LOCATION = 0
FIREWALL_LAYERS = {} #Layer, Depth
CAUGHT_LAYERS = {} #Layer, Depth
LOWEST_SAFE_WAIT = -1
PICOSECONDS_WAIT = 0
with open("Firewall_Layers.txt", "r") as layers:
    for layer in layers:
        removedCommas = layer.replace(':', '')
        elements = removedCommas.split()
        if int(elements[0]) > MAX_DEPTH:
            MAX_DEPTH = int(elements[0])
        FIREWALL_LAYERS[int(elements[0])] = int(elements[1])

def get_scanner_location(depth, time_counter):
    rotation_halves = math.floor(int(time_counter / (depth - 1)))
    scanner_location = None
    if rotation_halves % 2:
        scanner_location = depth - (time_counter % (depth - 1)) - 1
    else:
        scanner_location = time_counter % (depth - 1)
    return scanner_location

while LOWEST_SAFE_WAIT == -1:
    PICOSECOND_COUNTER = PICOSECONDS_WAIT
    CAUGHT_LAYERS = {}
    CURRENT_LOCATION = 0
    while CURRENT_LOCATION <= MAX_DEPTH:
        if CURRENT_LOCATION in FIREWALL_LAYERS:
            temp_depth = FIREWALL_LAYERS[CURRENT_LOCATION]
            rotation_halves = math.floor(int(PICOSECOND_COUNTER / (temp_depth - 1)))
            scanner_location = get_scanner_location(temp_depth, PICOSECOND_COUNTER)
            if scanner_location == 0:
                CAUGHT_LAYERS[CURRENT_LOCATION] = (temp_depth, PICOSECOND_COUNTER)
                break
            #print(f'{PICOSECOND_COUNTER}: Depth {temp_depth} on step {rotation_halves / 2}. The Scanner is at location {scanner_location}')
        PICOSECOND_COUNTER += 1
        CURRENT_LOCATION += 1
    if not CAUGHT_LAYERS:
        LOWEST_SAFE_WAIT = PICOSECONDS_WAIT
        break
    #print(f'{CAUGHT_LAYERS}')
    PICOSECONDS_WAIT += 1

print(f'The lowest safe waiting time (Part 2) is {PICOSECONDS_WAIT} picoseconds.')