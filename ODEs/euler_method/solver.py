# ---------------------------- importing packages ---------------------------- #
import numpy as np
from config.solverconfig import *
from plotting.plotter import *
from config.forwardconfig import *
from config.backwardconfig import *
from config.symplecticconfig import *

# -------------------------- choosing solver method and path ----------------- #
print("Please choose one of these approaches:\n1) Forward Euler Method\n" + \
    "2) Backward Euler Method\n3) Symplectic Euler Method")
solver_method = int(input())
file_path = "plotting/results/"
match solver_method:
    case 1:
        advance_interation_function = advance_iteration_by_forward_method
        file_path += "forwardresults.png"
    case 2:
        advance_interation_function = advance_iteration_by_backward_method
        file_path += "backwardresults.png"
    case 3:
        advance_interation_function = advance_iteration_by_symplectic_method
        file_path += "symplecticresults.png"

# ------------------------------ running solver ------------------------------ #
time_array = np.zeros(number_of_steps)
position_array =  np.zeros(number_of_steps)
position_array[0] = x_initial
velocity_array = np.zeros(number_of_steps)
velocity_array[0] = z_initial
x_previous = x_initial
z_previous = z_initial
x_updated = 0
z_updated = 0
for i in range(1, number_of_steps):
    # getting the (i-1)th values
    x_previous = position_array[i-1]
    z_previous = velocity_array[i-1]

    # calculating new values of x and z
    x_updated, z_updated = advance_interation_function(x_previous, z_previous)

    # storing new values of x and z
    time_array[i] = time_array[i-1] + h
    position_array[i] = x_updated
    velocity_array[i] = z_updated

# --------------------------- plotting the results --------------------------- #
plot_results(time_array, position_array, velocity_array, file_path)