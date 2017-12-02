import sys

LINE_INPUT = []

with open("mock_spreadsheet.txt", "r") as filestream:
    for line in filestream:
        LINE_INPUT.append(line)
sys.stdout.flush()

TOTAL_CHECKSUM = 0
CHECKSUM_COMPONENTS = []

while LINE_INPUT:
    A_LINE = LINE_INPUT.pop()
    LINE_ARRAY = A_LINE.split()
    LARGEST_NUM = None
    SMALLEST_NUM = None
    for a_number in LINE_ARRAY:
        if LARGEST_NUM is None or int(a_number) > LARGEST_NUM:
            LARGEST_NUM = int(a_number)
        if SMALLEST_NUM is None or int(a_number) < SMALLEST_NUM:
            SMALLEST_NUM = int(a_number)
    CHECKSUM_COMPONENTS.append(LARGEST_NUM - SMALLEST_NUM)

TOTAL_CHECKSUM = sum(CHECKSUM_COMPONENTS)
print(f'The Checksum for the Spreadsheet (Part 1) is {TOTAL_CHECKSUM}')