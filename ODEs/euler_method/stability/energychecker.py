# ---------------------------- importing packages ---------------------------- #
import numpy as np
from turtle import position
from config.solverconfig import *

# ---------------------------- defining functions ---------------------------- #
def calculate_total_energy(position_array, velocity_array):
    energy_array = np.zeros(len(position_array))
    for i in range(len(position_array)):
        calculated_kinetic_energy = 0.5 * m * velocity_array[i] ** 2
        calculated_potential_energy = 0.5 * alpha * m * position_array[i] ** 2
        energy_array[i] = calculated_kinetic_energy + calculated_potential_energy

    return energy_array  