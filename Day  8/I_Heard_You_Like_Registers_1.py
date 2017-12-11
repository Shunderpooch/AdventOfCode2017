import sys

REGISTERS = {}

def initialize_register(registerName):
    global REGISTERS
    REGISTERS.update({registerName: 0})

def run_command(registerShiftArray):
    global REGISTERS
    modifier = 0
    if registerShiftArray[0] not in REGISTERS:
        initialize_register(registerShiftArray[0])
    if registerShiftArray[1] == 'inc':
        modifier = 1
    elif registerShiftArray[1] == 'dec':
        modifier = -1
    else:
        raise Exception("An unrecognized modification was requested")
    REGISTERS[registerShiftArray[0]] += (int(registerShiftArray[2]) * modifier)

def run_register_change(inputLine):
    elements = inputLine.split()
    # if doesn't mean anything particulary, we know it will always be there
    comparison_register = elements[4]
    if comparison_register not in REGISTERS: # In the case it's not there, initialize it
        initialize_register(elements[4])
    if elements[5] == '==': # Equal Check
        if REGISTERS[elements[4]] == int(elements[6]):
            run_command(elements[:3])
        return
    elif elements[5] == '!=': # Not Equal Check
        if REGISTERS[elements[4]] != int(elements[6]):
            run_command(elements[:3])
        return
    elif elements[5] == '<': # Less Than Check
        if REGISTERS[elements[4]] < int(elements[6]):
            run_command(elements[:3])
        return
    elif elements[5] == '>': # Greater Than Check
        if REGISTERS[elements[4]] > int(elements[6]):
            run_command(elements[:3])
        return
    elif elements[5] == '<=': # Less Than or Equal Check
        if REGISTERS[elements[4]] <= int(elements[6]):
            run_command(elements[:3])
        return
    elif elements[5] == '>=': # Greater Than or Equal Check
        if REGISTERS[elements[4]] >= int(elements[6]):
            run_command(elements[:3])
        return
    else: 
        raise Exception("An unrecognized comparison was made, please check your file for errors.")

with open("Register_Instructions.txt", "r") as instructions:
    for line in instructions:
        run_register_change(line)

largest_val = None
for register_value in list(REGISTERS.values()):
    if largest_val is None or register_value > largest_val:
        largest_val = register_value

print(f'The largest value in any register at the end of the computations (Part 1) is {largest_val}')
            