# Author Arthur Dooner
# Advent of Code Day 12
# Part 2

class Program:
    def __init__(self, number, connections):
        self.number = number
        self.connections = connections

PROGRAMS = []
ALREADY_VISITED = []

def getNumConnected(programNum):
    global PROGRAMS
    # Assuming Programs in order
    tempNumConnected = 1
    ALREADY_VISITED.append(programNum)
    for connection in PROGRAMS[programNum].connections:
        if int(connection) not in ALREADY_VISITED:
            print(connection)
            tempNumConnected += getNumConnected(int(connection))
    return tempNumConnected


with open("Program_List.txt", "r") as programs:
    for program in programs:
        removedCommas = program.replace(',', ' ')
        elements = removedCommas.split()
        PROGRAMS.append(Program(int(elements[0]), elements[2:]))
    
print(f'The number of connections Program 0 has (Part 1) are: {getNumConnected(0)}')