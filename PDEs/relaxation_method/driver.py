# ---------------------------- importing packages ---------------------------- #
import numpy as np
from config import *
from solver import *
from convergence import *
from plotter import *

# ---------------------- initializing the voltage matrix --------------------- #
voltage_matrix = np.zeros((rows, columns))
voltage_matrix[:, 0] = np.ones(rows) * left_voltage
voltage_matrix[:, columns - 1] = np.ones(rows) * right_voltage
voltage_matrix[0, :] = np.ones(columns) * top_voltage
voltage_matrix[rows - 1, :] = np.ones(columns) * bottom_voltage

# -------------------------- iterating over the grid ------------------------- #
previous_sum = 0
new_sum = tolerance * 10
while not check_convergence(previous_sum, new_sum):
    for i in range(1, rows-1):
        for j in range(1, columns-1):
            voltage_matrix[i, j] = compute_weighted_average(voltage_matrix, i, j)
    
    previous_sum = new_sum
    new_sum = get_sum_of_matrix(voltage_matrix)

    print("current error: " + str(abs(new_sum - previous_sum)))

# --------------------------- plotting the results --------------------------- #
X = np.arange(0, height, hx)
Y = np.arange(0, width, hy)
X, Y = np.meshgrid(X, Y)
plot_surface(X, Y, voltage_matrix)

print("SUCCESS!")