# Author Arthur Dooner
# Advent of Code Day 18
# Part 1

INSTRUCTIONS = []
LAST_PLAYED_SOUND = None

def get_value(register_or_num, register_dict):
    if register_or_num.isalpha():
        if register_or_num not in register_dict:
            register_dict[register_or_num] = 0 # Initialize new values to 0
        return register_dict[register_or_num]
    else:
        return int(register_or_num)

def run_instruction(register_dict, an_instruction):
    global LAST_PLAYED_SOUND
    if len(an_instruction) == 2:
        if an_instruction[0] == "snd":
            LAST_PLAYED_SOUND = get_value(an_instruction[1], register_dict)
        elif an_instruction[0] == "rcv":
            if get_value(an_instruction[1], register_dict) != 0:
                print(f'The first value of the recovered frequency (Part 1) is {LAST_PLAYED_SOUND}')
                exit(0)
        else:
            raise Exception("An unrecognized command was given, and the program will exit.")
            exit(0)
    elif len(an_instruction) == 3:
        if an_instruction[0] == "add":
            register_dict[an_instruction[1]] = get_value(an_instruction[1], register_dict) + get_value(an_instruction[2], register_dict)
        elif an_instruction[0] == "jgz":
            if get_value(an_instruction[1], register_dict) > 0:
                return get_value(an_instruction[2], register_dict)
        elif an_instruction[0] == "mod":
            register_dict[an_instruction[1]] = get_value(an_instruction[1], register_dict) % get_value(an_instruction[2], register_dict)
        elif an_instruction[0] == "mul":
            register_dict[an_instruction[1]] = get_value(an_instruction[1], register_dict) * get_value(an_instruction[2], register_dict)
        elif an_instruction[0] == "set":
            register_dict[an_instruction[1]] = get_value(an_instruction[2], register_dict)
        else:
            raise Exception("An unrecognized command was given, and the program will exit.")
            exit(0)
    return 1

with open("Instructions.txt", "r") as instructions:
    for line in instructions:
        an_instruction = line.split()
        INSTRUCTIONS.append(an_instruction)

def run_instructions(all_instructions):
    instruction_index = 0
    instruction_change = 0
    registers = {}
    while instruction_index < len(all_instructions):
        instruction_change = run_instruction(registers, all_instructions[instruction_index])
        instruction_index += instruction_change

run_instructions(INSTRUCTIONS)
