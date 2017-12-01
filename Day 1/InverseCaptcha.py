import sys

LINE_INPUT = []

with open("input.txt", "r") as filestream:
    for line in filestream:
        LINE_INPUT.append(line)
sys.stdout.flush()

TOTAL_SUM = 0

while LINE_INPUT:
    ELEMENT = LINE_INPUT.pop()
    PREV_CHAR = None
    for char in ELEMENT:
        if PREV_CHAR is not None and char == PREV_CHAR:
            TOTAL_SUM += int(char)
        PREV_CHAR = char
    print(f'The compared strings are{ELEMENT[:1]} and {ELEMENT[len(ELEMENT)-1]}')
    if ELEMENT[:1] == ELEMENT[len(ELEMENT)-1:]:   
        TOTAL_SUM += int(ELEMENT[:1])

print(f'The Reverse Captcha is {TOTAL_SUM}')