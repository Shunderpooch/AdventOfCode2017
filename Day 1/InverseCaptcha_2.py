import sys

LINE_INPUT = []

with open("input.txt", "r") as filestream:
    for line in filestream:
        LINE_INPUT.append(line)
sys.stdout.flush()

TOTAL_SUM = 0

while LINE_INPUT:
    ELEMENT = LINE_INPUT.pop()
    ELEMENT_LENGTH = len(ELEMENT)
    counter = 0
    while counter < ELEMENT_LENGTH/2:
        NEXT_CHAR = ELEMENT[int(counter + ELEMENT_LENGTH/2):int(counter + 1 + ELEMENT_LENGTH/2)]
        if ELEMENT[int(counter):int(counter + 1)] == NEXT_CHAR:
            TOTAL_SUM += int(NEXT_CHAR)
        counter += 1
    TOTAL_SUM *= 2

print(f'The Reverse Captcha Part 2 is {TOTAL_SUM}')