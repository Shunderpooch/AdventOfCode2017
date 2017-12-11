import sys

LINE_INPUT = []

with open("passphrases.txt", "r") as filestream:
    for line in filestream:
        LINE_INPUT.append(line)
sys.stdout.flush()

TOTAL_VALID_PASSPHRASES = 0
VALID_PASSPHRASES = []

def are_Words_Anagrams(firstWord, secondWord):
    firstWordList = list(firstWord)
    secondWordList = list(secondWord)
    for character in firstWordList:
        if character in secondWordList:
            secondWordList.remove(character)
        else:
            return False
    # We've exhausted the first word list and there are still elements in the second word list
    if secondWordList:
        return False
    else:
        return True
def is_Valid_Passphrase(aLine):
    tempLine = aLine
    lineArray = tempLine.split()
    aWord = lineArray.pop()
    while lineArray:
        for aTempWord in lineArray:
            if are_Words_Anagrams(aWord, aTempWord):
                return False
        aWord = lineArray.pop()
    return True

while LINE_INPUT:
    A_LINE = LINE_INPUT.pop()
    output_passphrase = []
    if is_Valid_Passphrase(A_LINE):
        output_passphrase.append(A_LINE)
        TOTAL_VALID_PASSPHRASES += 1

    
print(f'The Total Valid Passphrases for Part 2 are {TOTAL_VALID_PASSPHRASES}')