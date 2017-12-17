# Author Arthur Dooner
# Advent of Code Day 16
# Part 1, "Permutation Promenade"

DANCE_COMMANDS = []
DANCE_ELEMENTS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
def move_end_to_front(num_elements, a_list):
    # print(a_list)
    # print(num_elements)
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
with open("Dance.txt", "r") as layers:
    for layer in layers:
        removedCommas = layer.replace(',', ' ')
        elements = removedCommas.split()
        for element in elements:
            if element[0] == "s":
                DANCE_ELEMENTS = move_end_to_front(int(element[1:]), DANCE_ELEMENTS)
            elif element[0] == "x":
                loc_of_dash = element.index('/')
                switch_places(int(element[1:loc_of_dash]), int(element[(loc_of_dash + 1):]), DANCE_ELEMENTS)
            elif element[0] == "p":
                loc_of_dash = element.index('/')
                switch_places_value(element[1:loc_of_dash], element[(loc_of_dash + 1):], DANCE_ELEMENTS)
        # if int(elements[0]) > DANCE_COMMANDS:
        #     MAX_DEPTH = int(elements[0])
        # FIREWALL_LAYERS[int(elements[0])] = int(elements[1])
output = ''.join(DANCE_ELEMENTS)
print(f'The order of the elements at the end of the dance (Part 1) are {output}')