import sys

def program_info(inputLine):
    removedCommas = inputLine.replace(',', '')
    elements = removedCommas.split()
    if (len(elements) < 3):
        return elements[0], []
    else:
        return elements[0], elements[3:]

ParentProgramList = []
ParentsChildren = []
with open("Program_List.txt", "r") as memoryBlocks:
    for line in memoryBlocks:
        process_name, sub_processes = program_info(line)
        if (len(sub_processes) > 0):
            ParentProgramList.append(process_name)
            ParentsChildren.extend(sub_processes)

for element in ParentProgramList:
    if element in ParentsChildren:
        continue
    else:
        print(f'The name of the bottom program (Part 1) is {element}')
        exit(0)
            