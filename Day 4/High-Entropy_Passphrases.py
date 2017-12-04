import sys

LINE_INPUT = []

with open("passphrases.txt", "r") as filestream:
    for line in filestream:
        LINE_INPUT.append(line)
sys.stdout.flush()

TOTAL_VALID_PASSPHRASES = 0
VALID_PASSPHRASES = []

def is_Valid_Passphrase(aLine):
    tempLine = aLine
    lineArray = tempLine.split()
    aWord = lineArray.pop()
    while lineArray:
        if aWord in lineArray:
            return False
        aWord = lineArray.pop()
    return True

while LINE_INPUT:
    A_LINE = LINE_INPUT.pop()
    output_passphrase = []
    if is_Valid_Passphrase(A_LINE):
        output_passphrase.append(A_LINE)
        TOTAL_VALID_PASSPHRASES += 1

    
print(f'The Total Valid Passphrases for (Part 1) are {TOTAL_VALID_PASSPHRASES}')