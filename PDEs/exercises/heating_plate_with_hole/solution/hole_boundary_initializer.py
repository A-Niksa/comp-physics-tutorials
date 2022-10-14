# importing config and geometry manager
from config import *
import geometry_manager as geo


# defining the hole boundary conditions imposing functions
def set_hole_boundary_conditions(nodes_matrix):
    # left boundary:
    column_index, row_start_index, row_end_index = geo.get_hole_left_indices()
    nodes_matrix[row_start_index:row_end_index, column_index] = hole_left_temperature

    # right boundary:
    column_index, row_start_index, row_end_index = geo.get_hole_right_indices()
    nodes_matrix[row_start_index:row_end_index, column_index] = hole_left_temperature

    # top boundary:
    row_index, column_start_index, column_end_index = geo.get_hole_top_indices()
    nodes_matrix[row_index, column_start_index:column_end_index] = hole_top_temperature

    # bottom boundary:
    row_index, column_start_index, column_end_index = geo.get_hole_bottom_indices()
    nodes_matrix[row_index, column_start_index:column_end_index] = hole_bottom_temperature


def set_hole_temperature(nodes_matrix):
    for i in range(rows):
        for j in range(columns):
            if geo.is_inside_hole(i, j):
                nodes_matrix[i, j] = default_hole_temperature
