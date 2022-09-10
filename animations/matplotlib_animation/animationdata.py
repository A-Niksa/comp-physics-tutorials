# ---------------------------- importing packages ---------------------------- #
import numpy as np
from config import *

# ---------------------------- defining functions ---------------------------- #
def get_animation_data():
    time_array = np.linspace(0, t_end, n)

    angular_frequency = np.sqrt(2 * g * mu / l)
    position_array = x_initial * np.cos(angular_frequency * time_array)

    return time_array, position_array