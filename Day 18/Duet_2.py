# Author Arthur Dooner
# Advent of Code Day 18
# Part 2

from multiprocessing import Process, Pipe, Lock

def get_value(register_or_num, register_dict):
    if register_or_num.isalpha():
        if register_or_num not in register_dict:
            register_dict[register_or_num] = 0 # Initialize new values to 0
        return register_dict[register_or_num]
    else:
        return int(register_or_num)

def run_instruction(register_dict, an_instruction, a_pipe, program_counter):
    if len(an_instruction) == 2:
        if an_instruction[0] == "snd":
            a_pipe.send(get_value(an_instruction[1], register_dict))
            program_counter += 1
        elif an_instruction[0] == "rcv":
            if a_pipe.poll(1):
                register_dict[an_instruction[1]] = int(a_pipe.recv())
            else:
                raise EOFError("Done with the program")
        else:
            raise Exception("An unrecognized command was given, and the program will exit.")
            exit(0)
    elif len(an_instruction) == 3:
        if an_instruction[0] == "add":
            register_dict[an_instruction[1]] = get_value(an_instruction[1], register_dict) + get_value(an_instruction[2], register_dict)
        elif an_instruction[0] == "jgz":
            if get_value(an_instruction[1], register_dict) > 0:
                return get_value(an_instruction[2], register_dict), program_counter
        elif an_instruction[0] == "mod":
            register_dict[an_instruction[1]] = get_value(an_instruction[1], register_dict) % get_value(an_instruction[2], register_dict)
        elif an_instruction[0] == "mul":
            register_dict[an_instruction[1]] = get_value(an_instruction[1], register_dict) * get_value(an_instruction[2], register_dict)
        elif an_instruction[0] == "set":
            register_dict[an_instruction[1]] = get_value(an_instruction[2], register_dict)
        else:
            raise Exception("An unrecognized command was given, and the program will exit.")
            exit(0)
    return 1, program_counter

def run_instructions(all_instructions, p_state, a_pipe, program_counter):
    instruction_index = 0
    instruction_change = 0
    registers = {}
    registers['p'] = p_state
    while instruction_index < len(all_instructions):
        try:
            instruction_change, program_counter = run_instruction(registers, all_instructions[instruction_index], a_pipe, program_counter)
        except EOFError as identifier:
            if (p_state == 1):
                print(f'Program {p_state} (Part 2) sent {program_counter} programs.')
            exit(0)
        instruction_index += instruction_change

if __name__ == "__main__":
    INSTRUCTIONS = []
    with open("Instructions.txt", "r") as instructions:
        for line in instructions:
            an_instruction = line.split()
            INSTRUCTIONS.append(an_instruction)
    connection_left, connection_right = Pipe()
    Program0Counter = 0
    Program1Counter = 0
    program_0 = Process(target=run_instructions, args=(INSTRUCTIONS, 0, connection_left, Program0Counter))
    program_1 = Process(target=run_instructions, args=(INSTRUCTIONS, 1, connection_right, Program1Counter))
    program_0.start()
    program_1.start()
    program_0.join()
    program_1.join()
        