# Author Arthur Dooner
# Advent of Code Day 14
# Part 1

import sys

BASE_KNOT_HASH = []
ARRAY_SIZE = 256
LIST_TO_USE = list(range(0, ARRAY_SIZE))
CURRENT_INDEX = 0
SKIP_SIZE = 0
NUMBER_RUNS = 64
NUMBER_HASH_ROWS = 128
if len(sys.argv) != 2:
    print(f'Invalid input! Please write your key string after the program name.')
    exit(0)
BASE_KNOT_HASH = sys.argv[1] # My puzzle input was 'wenycdww'

def get_sub_array(starting_index, ending_index, result_list):
    if ending_index <= starting_index:
        temp_list = result_list[starting_index:]
        temp_list.extend(result_list[:ending_index])
        return temp_list
    else:
        return result_list[starting_index:ending_index]

def set_sub_array(starting_index, ending_index, new_sub_array, result_list):
    if ending_index <= starting_index:
        result_list[starting_index:] = new_sub_array[:(len(result_list) - starting_index)]
        result_list[:ending_index] = new_sub_array[(len(result_list) - starting_index):]
    else:
        result_list[starting_index:ending_index] = new_sub_array

def knot_hash(inputArray):
    counter = 0
    global NUMBER_RUNS, ARRAY_SIZE
    temp_index = 0
    temp_skip_size = 0
    result_list = list(range(0, ARRAY_SIZE))
    # Loop a set number of times
    while counter < NUMBER_RUNS:
        for a_length in inputArray:
            if int(a_length) != 0: # Need to catch the 0 case
                temp_array = get_sub_array(temp_index, (temp_index + int(a_length)) % ARRAY_SIZE, result_list)
                temp_array.reverse() # Reverse the array
                set_sub_array(temp_index, (temp_index + int(a_length)) % ARRAY_SIZE, temp_array, result_list)
            # print(LIST_TO_USE)
            temp_index = (temp_index + int(a_length) + temp_skip_size) % ARRAY_SIZE
            temp_skip_size += 1
        counter += 1
    return generate_dense_hash(result_list)

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

def convert_to_binary_string(byte_array):
    return ''.join(list(map(lambda b: format(b, '08b'), byte_array)))

i = 0
RESULT = 0
while i < NUMBER_HASH_ROWS:
    temp_byte_array = bytearray(str.encode(f'{BASE_KNOT_HASH}-{i}'))
    # print(f'{BASE_KNOT_HASH}-{i}')
    temp_byte_array.extend([17, 31, 73, 47, 23])
    row_output = convert_to_binary_string(knot_hash(temp_byte_array))
    # print(f'{row_output}')
    for char in row_output:
        if char == "1":
            RESULT += 1
    i += 1

print(f'The total number of squares used in the grid (Part 1) are {RESULT}')