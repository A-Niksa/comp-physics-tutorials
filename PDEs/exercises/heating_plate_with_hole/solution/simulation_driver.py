# importing necessary packages and modules:
import numpy as np
import node_averaging_calculator as calc
import plotter as splt  # splt is the short form of surface plot
import geometry_manager as geo
import convergence_checker as cnvrg
import hole_boundary_initializer as bdry
from config import *

# initializing the nodes' matrix and imposing the plate outer boundary conditions
nodes_matrix = np.ones((rows, columns)) * initial_plate_temperature
nodes_matrix[:, 0] = plate_left_temperature
nodes_matrix[:, columns - 1] = plate_right_temperature
nodes_matrix[0, :] = plate_top_temperature
nodes_matrix[rows - 1, :] = plate_bottom_temperature

# imposing the hole boundary conditions:
bdry.set_hole_boundary_conditions(nodes_matrix)

# iterating over the nodes:
previous_sum = 0
new_sum = tolerance * 10
while not cnvrg.check_convergence(previous_sum, new_sum):
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            if not geo.is_inside_hole(i, j):
                nodes_matrix[i, j] = calc.calculate_neighboring_nodes_average(nodes_matrix, i, j)

    previous_sum = new_sum
    new_sum = cnvrg.get_sum_of_nodes_matrix(nodes_matrix)

    print("current error: " + str(abs(new_sum - previous_sum)))

# removing the hole from the plate for graphical purposes:
bdry.set_hole_temperature(nodes_matrix, default_hole_temperature)

# plotting the results:
x_array = np.arange(0, plate_height, hx)
y_array = np.arange(0, plate_width, hy)
x_matrix, y_matrix = np.meshgrid(x_array, y_array)
splt.plot_surface(x_matrix, y_matrix, nodes_matrix)


print("SUCCESS!")
