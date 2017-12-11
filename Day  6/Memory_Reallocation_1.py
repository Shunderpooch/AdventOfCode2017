import sys

MemoryList = []
with open("Initial_Memory_Block_Counts.txt", "r") as memoryBlocks:
    for line in memoryBlocks:
        for anElement in line.split():
            MemoryList.append(int(anElement))
        

previousLists = [] #this is a list logging past lists
def compareWithPreviousLists(listToCompare):
    global previousLists
    for aList in previousLists:
        if aList == listToCompare:
            return True
    return False

counter = 0

while not compareWithPreviousLists(MemoryList):
    previousLists.append(MemoryList[:])
    largestVal = max(MemoryList)
    tempIndex = MemoryList.index(largestVal) #gets the index of the largest value
    # First set largest val to 0 using the index
    MemoryList[tempIndex] = 0 # Take everything out of the memory bank
    while largestVal:
        tempIndex += 1
        if tempIndex == len(MemoryList):
            tempIndex = 0
        MemoryList[tempIndex] += 1
        largestVal -= 1
    counter += 1

print("The number of redistribution cycles before a configuration is produced that has been seen before is " + str(counter))