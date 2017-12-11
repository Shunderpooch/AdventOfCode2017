import sys

INPUT_LENGTHS = []
ARRAY_SIZE = 256
LIST_TO_USE = list(range(0, ARRAY_SIZE))
CURRENT_INDEX = 0
SKIP_SIZE = 0
NUMBER_RUNS = 64

with open("Input_Lengths.txt", "r") as inputLengths:
    for line in inputLengths:
        elements = bytearray(str.encode(line))
        INPUT_LENGTHS.extend(elements)
# add the standard length suffix values
INPUT_LENGTHS.extend([17, 31, 73, 47, 23])
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

COUNTER = 0
# Loop a set number of times
while COUNTER < NUMBER_RUNS:
    for aLength in INPUT_LENGTHS:
        if int(aLength) != 0: # Need to catch the 0 case
            temp_array = get_sub_array(CURRENT_INDEX, (CURRENT_INDEX + int(aLength)) % ARRAY_SIZE)
            temp_array.reverse() # Reverse the array
            set_sub_array(CURRENT_INDEX, (CURRENT_INDEX + int(aLength)) % ARRAY_SIZE, temp_array)
        # print(LIST_TO_USE)
        CURRENT_INDEX = (CURRENT_INDEX + int(aLength) + SKIP_SIZE) % ARRAY_SIZE
        SKIP_SIZE += 1
    COUNTER += 1

### Result at this point is a sparse hash
def xor_16(input_values):
    output = 0
    for element in input_values:
        output = output ^ element
    return output

def generate_dense_hash(sparse_hash):
    dense_hash = []
    sparse_hash_counter = 0
    while sparse_hash_counter < 256:
        dense_hash.append(xor_16(sparse_hash[sparse_hash_counter:(sparse_hash_counter + 16)]))
        sparse_hash_counter += 16
    return dense_hash

DENSE_HASH_OUTPUT = generate_dense_hash(LIST_TO_USE)

def convert_to_hex_string(byte_array):
    return ''.join(list(map(lambda x: format(x, 'x'), byte_array)))

print(f'The Knot Hash of my puzzle input (Part 2) is: {convert_to_hex_string(DENSE_HASH_OUTPUT)}')