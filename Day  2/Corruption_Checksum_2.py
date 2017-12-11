import sys

LINE_INPUT = []

with open("mock_spreadsheet.txt", "r") as filestream:
    for line in filestream:
        LINE_INPUT.append(line)
sys.stdout.flush()

TOTAL_CHECKSUM = 0
CHECKSUM_COMPONENTS = []

def get_evenly_divisible(A_LINE_LIST):
    # Sort the list since most divisible will be first
    A_LINE_LIST.sort(reverse=True)
    while A_LINE_LIST:
        # Pop off the smallest element
        cell_to_compare = A_LINE_LIST.pop()
        # Iterate over the remainder from greatest to least 
        for a_bigger_cell in A_LINE_LIST:
            # A lot of ways to check this, but really trying to gather if the number is whole
            if (a_bigger_cell/cell_to_compare).is_integer():
                return int(a_bigger_cell/cell_to_compare)


while LINE_INPUT:
    A_LINE = LINE_INPUT.pop()
    LINE_ARRAY = [float(x) for x in A_LINE.split()]
    CHECKSUM_COMPONENTS.append(get_evenly_divisible(LINE_ARRAY))

TOTAL_CHECKSUM = sum(CHECKSUM_COMPONENTS)
print(f'The Checksum for the Spreadsheet (Part 2) is {TOTAL_CHECKSUM}')
