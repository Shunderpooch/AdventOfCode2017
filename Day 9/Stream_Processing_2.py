import sys

STREAM = []

with open("stream.txt", "r") as inputStream:
    for line in inputStream:
        STREAM.extend(list(line))

inGarbage = False
isNegated = False
additiveScore = 0
groupDepth = 0
garbageCount = 0
for element in STREAM:
    if isNegated:
        isNegated = False
        continue
    if not inGarbage:
        if element == '{':
            groupDepth += 1
            additiveScore += groupDepth
        elif element == '}':
            groupDepth -= 1
        elif element == '<':
            inGarbage = True
    else: # The case we're in garbage
        if element == '!':
            isNegated = True
        elif element == '>': # Already catching the case 
            inGarbage = False
        else:
            garbageCount += 1

print(f'The total removed characters in garbage (Part 2) is {garbageCount} characters')