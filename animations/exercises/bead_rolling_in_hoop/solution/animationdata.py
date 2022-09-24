# ---------------------------- importing packages ---------------------------- #
import numpy as np
from config import *

# ---------------------------- defining functions ---------------------------- #
def get_animation_data():
    time_array = np.linspace(0, t_end, n)

    angular_frequency = np.sqrt((5/7 * m * g / R))
    angle_array = theta_initial * np.cos(angular_frequency * time_array)
    x_position_array = -R * np.sin(angle_array) + r * np.sin(angle_array)
    y_position_array = -R * np.cos(angle_array) + r * np.cos(angle_array)
                                
    return time_array, angle_array, x_position_array, y_position_array