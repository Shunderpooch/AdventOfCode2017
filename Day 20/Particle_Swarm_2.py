# Author Arthur Dooner
# Advent of Code Day 20
# Part 2 "Particle Swarm"

import math
import numpy as np

ALL_PARTICLES = []
POTENTIAL_COLLISIONS = []
counter = 0
marked_counter = 0

# The math here to be efficient requires Newton's method

class Particle:
    def __init__(self, particle_id, position, velocity, acceleration):
        self.particle_id = particle_id
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def directional_equality(self, position_0, velocity_0, acceleration_0, position_1, velocity_1, acceleration_1):
        # So the distance formula is 1/2at^2 + vt + p = result
        # We need to augment the half of step and add + 1/2at
        coefficients = [float(acceleration_0 - acceleration_1)*(.5), velocity_0 - velocity_1 + (.5) * float(acceleration_0) - (.5) * float(acceleration_1), position_0 - position_1]
        #print(coefficients)
        return np.roots(coefficients)

    def will_collide(self, another_particle):
        global POTENTIAL_COLLISIONS
        counter = 0
        all_roots = []
        while counter < len(self.position):
            temp_roots = self.directional_equality(self.position[counter], self.velocity[counter], self.acceleration[counter], 
                another_particle.position[counter], another_particle.velocity[counter], another_particle.acceleration[counter])
            temp_result_roots = temp_roots.tolist()
            temp_counter = 0
            while temp_counter < len(temp_result_roots):
                if (isinstance(temp_result_roots[temp_counter], complex)):
                    return
                else:
                    temp_result_roots[temp_counter] = round(temp_result_roots[temp_counter])
                temp_counter += 1
            all_roots.append(set(temp_result_roots))
            #print(all_roots)
            counter += 1
        counter = 0
        # print(*all_roots)
        result_set = set.intersection(*all_roots)
        # At this point we have all possible roots. We check for collisions here and filter out imaginary ones and ones with negative (before time index 0) roots
        for element in result_set:
            if element >= 0:
                # print(result_set)
                # print("Made it here")
                answer = self.check_answer(element, another_particle, True)
                if answer >= 0:
                    POTENTIAL_COLLISIONS.append([self.particle_id, another_particle.particle_id, element])
                    return True
                else:
                    return False
                    

with open("Particles.txt", "r") as Particles:
    for particle in Particles:
        Particle_Components = particle.split()
        elements_to_remove = ['p=<', 'v=<', 'a=<']
        element_counter = 0
        result_lists = []
        while element_counter < len(Particle_Components):
            a_state = Particle_Components[element_counter]
            a_state = a_state.replace(elements_to_remove[element_counter], '')
            a_state = a_state.replace('>', '')
            a_state = a_state.replace(',', ' ')
            a_state = [int(x) for x in a_state.split()] # Convert to ints
            result_lists.append(a_state)
            element_counter += 1
        a_particle = Particle(counter, result_lists[0], result_lists[1], result_lists[2])
        ALL_PARTICLES.append(a_particle)
        counter += 1

counter = 0
num_particles = len(ALL_PARTICLES)
# Need to take the element out and compare it with the rest
while counter < len(ALL_PARTICLES):
    a_particle = ALL_PARTICLES.pop(counter) # Remove it
    # Compare it against everything else
    # print(f'Comparing all particles against particle {a_particle.particle_id}')
    for particle_to_compare in ALL_PARTICLES:
        a_particle.will_collide(particle_to_compare)

def get_a_time(item):
    return item[2]

POTENTIAL_COLLISIONS.sort(key=get_a_time)

deleted_items = set()
a_time = 0
while a_time <= POTENTIAL_COLLISIONS[len(POTENTIAL_COLLISIONS) - 1][2]: # Get the last unit of time
    temp_deleted_items = set()
    current_items = filter(lambda item: item[2] == a_time, POTENTIAL_COLLISIONS)
    for item in current_items:
        print(a_time)
        if item[0] not in deleted_items and item[1] not in deleted_items:
            temp_deleted_items.add(item[0])
            temp_deleted_items.add(item[1])
        print(temp_deleted_items)
    deleted_items = deleted_items.union(temp_deleted_items)
    a_time += 1

answer = num_particles - len(deleted_items)
print(f'The number of particles remaining after the collisions are resolved are: {num_particles - len(deleted_items)}')
