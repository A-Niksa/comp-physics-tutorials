# importing necessary packages:
import geometry_manager as geo
from config import *


# defining convergence checking functions
def check_convergence(previous_sum, new_sum):
    return abs(new_sum - previous_sum) < tolerance


def get_sum_of_nodes_matrix(nodes_matrix):
    nodes_matrix_sum = 0.0
    for i in range(rows):
        for j in range(columns):
            if not geo.is_inside_hole(i, j):
                nodes_matrix_sum += nodes_matrix[i, j]

    return nodes_matrix_sum
