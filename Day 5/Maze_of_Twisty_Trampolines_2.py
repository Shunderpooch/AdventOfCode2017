import sys

JUMP_OFFSETS = []

with open("maze.txt", "r") as filestream:
    for line in filestream:
        JUMP_OFFSETS.append(int(line)) #Convert to int as we go

sys.stdout.flush()

CURRENT_INDEX = 0
NUM_STEPS = 0
while CURRENT_INDEX >= 0 and CURRENT_INDEX < len(JUMP_OFFSETS):
    PREV_INDEX = CURRENT_INDEX
    CURRENT_INDEX += JUMP_OFFSETS[CURRENT_INDEX]
    if JUMP_OFFSETS[PREV_INDEX] >= 3:
        JUMP_OFFSETS[PREV_INDEX] -= 1
    else:
        JUMP_OFFSETS[PREV_INDEX] += 1
    NUM_STEPS += 1

print(f'The number of steps to exit the maze from Part 2 are {NUM_STEPS}')