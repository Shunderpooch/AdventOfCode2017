# Author Arthur Dooner
# Advent of Code Day 19
# Part 2

ROUTING_GRID = []

with open("Routing_Diagram.txt", "r") as routes:
    for line in routes:
        ROUTING_GRID.append(line)

def get_starting_point(grid):
    y_counter = 0
    for y_line in grid:
        x_counter = 0
        for a_x in y_line:
            if a_x == "|" or a_x == "-": # Only gonna ever start with a direction pulling off
                return x_counter, y_counter
            x_counter += 1
        y_counter += 1

def get_direction(previous_loc, current_loc):
    if current_loc[1] > previous_loc[1]: # We're going further down on Y
        return "South"
    elif current_loc[1] < previous_loc[1]:
        return "North"
    elif current_loc[0] > previous_loc[0]:
        return "West"
    elif current_loc[0] < previous_loc[0]:
        return "East"

def get_connections(current_loc, grid):
    connections = []
    if (current_loc[1] > 0): # As long as the Y value is greater than 0
        if (grid[current_loc[1] - 1][current_loc[0]]) == "|": # A connection above
            connections.append((current_loc[0], current_loc[1] - 1))
    if (current_loc[1] < len(grid) - 1): # As long as the Y value is smaller than the largest one
        if (grid[current_loc[1] + 1][current_loc[0]]) == "|": # A connection below
            connections.append((current_loc[0], current_loc[1] + 1))
    if (current_loc[0] > 0): # As long as the X value is greater than 0
        if (grid[current_loc[1]][current_loc[0] - 1]) == "-": # A connection to the left
            connections.append((current_loc[0] - 1, current_loc[1]))
    if (current_loc[0] < len(grid[current_loc[1]]) - 1): # As long as the X value is smaller than the largest one
        if (grid[current_loc[1]][current_loc[0] + 1]) == "-": # A connection to the right
            connections.append((current_loc[0] + 1, current_loc[1]))
    return connections

def get_new_direction(current_loc, direction, grid):
    if grid[current_loc[1]][current_loc[0]] == "+": # We're at a crossroads
        transition = get_connections(current_loc, grid) # Get the connections a plus has
        if direction == "North":
            transition.remove((current_loc[0], current_loc[1] + 1)) # Remove the element from the South
            return get_direction(current_loc, transition[0])
        elif direction == "South":
            transition.remove((current_loc[0], current_loc[1] - 1)) # Remove the element from the North
            return get_direction(current_loc, transition[0])
        elif direction == "West":
            transition.remove((current_loc[0] - 1, current_loc[1])) # Remove the element from the East
            return get_direction(current_loc, transition[0])
        elif direction == "East":
            transition.remove((current_loc[0] + 1, current_loc[1])) # Remove the element from the West
            return get_direction(current_loc, transition[0])
    return direction


X_INDEX, Y_INDEX = get_starting_point(ROUTING_GRID)
A_DIRECTION = "South" # Inital State

VISITED_LETTERS = ""

ALL_STEPS = 0

while ROUTING_GRID[Y_INDEX][X_INDEX] is not " ":
    
    if ROUTING_GRID[Y_INDEX][X_INDEX].isalpha():
        VISITED_LETTERS += ROUTING_GRID[Y_INDEX][X_INDEX]
    else:
        A_DIRECTION = get_new_direction((X_INDEX, Y_INDEX), A_DIRECTION, ROUTING_GRID)
    if A_DIRECTION == "South":
        Y_INDEX += 1
    elif A_DIRECTION == "North":
        Y_INDEX -= 1
    elif A_DIRECTION == "West":
        X_INDEX += 1
    elif A_DIRECTION == "East":
        X_INDEX -= 1
    ALL_STEPS += 1
    

print(f"The number of steps that must be taken (Part 2) is {ALL_STEPS}")