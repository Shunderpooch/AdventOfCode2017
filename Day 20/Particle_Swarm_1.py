# Author Arthur Dooner
# Advent of Code Day 20
# Part 1 "Particle Swarm"

import math

minimum_acceleration = None # Measuring Manhattan Distance so simply additive
counter = 0
marked_counter = 0

with open("Particles.txt", "r") as Particles:
    for particle in Particles:
        an_acceleration = (particle.split())[2]
        an_acceleration = an_acceleration.replace('a=<', '')
        an_acceleration = an_acceleration.replace('>', '')
        an_acceleration = an_acceleration.replace(',', ' ')
        an_acceleration = [int(x) for x in an_acceleration.split()] # Convert to ints
        acceleration_magnitude = sum([abs(x) for x in an_acceleration])
        if minimum_acceleration is None or acceleration_magnitude < minimum_acceleration:
            minimum_acceleration = acceleration_magnitude
            marked_counter = counter
        counter += 1

print(f'Particle {marked_counter} is the one that will remain closest to the origin over the longest frame of time')