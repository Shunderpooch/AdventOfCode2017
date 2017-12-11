import sys

INPUT_LENGTHS = []
ARRAY_SIZE = 256
LIST_TO_USE = list(range(0, ARRAY_SIZE))
CURRENT_INDEX = 0
SKIP_SIZE = 0

with open("Input_Lengths.txt", "r") as inputLengths:
    for line in inputLengths:
        removedCommas = line.replace(',', ' ')
        elements = removedCommas.split()
        INPUT_LENGTHS.extend(elements)

def get_sub_array(starting_index, ending_index):
    global LIST_TO_USE
    if ending_index <= starting_index:
        temp_list = LIST_TO_USE[starting_index:]
        temp_list.extend(LIST_TO_USE[:ending_index])
        return temp_list
    else:
        return LIST_TO_USE[starting_index:ending_index]

def set_sub_array(starting_index, ending_index, new_sub_array):
    global LIST_TO_USE
    if ending_index <= starting_index:
        LIST_TO_USE[starting_index:] = new_sub_array[:(len(LIST_TO_USE) - starting_index)]
        LIST_TO_USE[:ending_index] = new_sub_array[(len(LIST_TO_USE) - starting_index):]
    else:
        LIST_TO_USE[starting_index:ending_index] = new_sub_array

for aLength in INPUT_LENGTHS:
    if (int(aLength) != 0): # Need to catch the 0 case
        temp_array = get_sub_array(CURRENT_INDEX, (CURRENT_INDEX + int(aLength)) % ARRAY_SIZE)
        temp_array.reverse() # Reverse the array
        set_sub_array(CURRENT_INDEX, (CURRENT_INDEX + int(aLength)) % ARRAY_SIZE, temp_array)
    # print(LIST_TO_USE)
    CURRENT_INDEX = (CURRENT_INDEX + int(aLength) + SKIP_SIZE) % ARRAY_SIZE
    SKIP_SIZE += 1

print(f'The result of multiplying the first two numbers in the list (Part 1) is {LIST_TO_USE[0] * LIST_TO_USE[1]}')
