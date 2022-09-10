# ------------------------ importing necessary modules ----------------------- #
import math
import numpy as np
from config.solverconfig import *

# ---------------------------- defining functions ---------------------------- #
def calculate_analyitic_results(time_array):
    angular_frequency = math.sqrt(2 * g * mu / l)
    analytic_position_array = np.zeros(number_of_steps)
    for i in range(number_of_steps):
        analytic_position_array[i] = x_initial * math.cos(angular_frequency * time_array[i])
    
    return analytic_position_array