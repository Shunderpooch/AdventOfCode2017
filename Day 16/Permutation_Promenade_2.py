# Author Arthur Dooner
# Advent of Code Day 16
# Part 2, "Permutation Promenade"

DANCE_COMMANDS = []
DANCE_ELEMENTS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
ALL_ITERATIONS = 1000000000
def move_end_to_front(num_elements, a_list):
    a_list = a_list[(-1 * num_elements):] + a_list[:(-1 * num_elements)]
    return a_list

def switch_places(loc_1, loc_2, a_list):
    temp_element_1 = a_list[loc_1]
    temp_element_2 = a_list[loc_2]
    a_list[loc_1] = temp_element_2
    a_list[loc_2] = temp_element_1
    
def switch_places_value(val_1, val_2, a_list):
    temp_index_1 = a_list.index(val_1)
    temp_index_2 = a_list.index(val_2)
    a_list[temp_index_1] = val_2
    a_list[temp_index_2] = val_1

def run_dance(dancers, commands):
    for command in commands:
        if command[0] == "s":
            dancers = move_end_to_front(int(command[1:]), dancers)
        elif command[0] == "x":
            loc_of_dash = command.index('/')
            switch_places(int(command[1:loc_of_dash]), int(command[(loc_of_dash + 1):]), dancers)
        elif command[0] == "p":
            loc_of_dash = command.index('/')
            switch_places_value(command[1:loc_of_dash], command[(loc_of_dash + 1):], dancers)
    return dancers

DANCE_COMMANDS = []
with open("Dance.txt", "r") as layers:
    for layer in layers:
        removedCommas = layer.replace(',', ' ')
        DANCE_COMMANDS.extend(removedCommas.split())

iteration_num = 0
ITERATION_REPEAT = 0
DANCE_HISTORY = []
while iteration_num < ALL_ITERATIONS:
    DANCE_ELEMENTS = run_dance(DANCE_ELEMENTS, DANCE_COMMANDS)
    if (DANCE_ELEMENTS in DANCE_HISTORY):
        ITERATION_REPEAT = iteration_num
        break
    else:
        DANCE_HISTORY.append(DANCE_ELEMENTS)
    DANCE_ELEMENTS = DANCE_ELEMENTS[:]
    iteration_num += 1

output = ''.join(DANCE_HISTORY[(ALL_ITERATIONS % ITERATION_REPEAT) - 1])
print(f'The order of the elements at the end of {ALL_ITERATIONS} dances (Part 2) are {output}')