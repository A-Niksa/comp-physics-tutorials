# importing config:
from config import *


# defining the functions that let us know if the node at (i, j) is inside the hole:
def is_inside_hole(i, j):
    relative_i = i / rows
    relative_j = j / columns

    return is_index_in_hole(relative_i, True) and is_index_in_hole(relative_j, False)


def is_index_in_hole(relative_index, is_row_index):
    if is_row_index:
        relative_hole_start_index = (plate_height - hole_height) / (2.0 * plate_height)
        relative_hole_end_index = (plate_height + hole_height) / (2.0 * plate_height)
    else:
        relative_hole_start_index = (plate_width - hole_width) / (2.0 * plate_width)
        relative_hole_end_index = (plate_width + hole_width) / (2.0 * plate_width)

    return relative_hole_start_index <= relative_index <= relative_hole_end_index


# defining the functions that give us the hole boundary indices:
def get_hole_left_indices():
    relative_column_start_index, relative_column_end_index = get_relative_column_indices()
    relative_row_start_index, relative_row_end_index = get_relative_row_indices()

    column_index = int(columns * relative_column_start_index)
    row_start_index = int(rows * relative_row_start_index)
    row_end_index = int(rows * relative_row_end_index)
    return column_index, row_start_index, row_end_index


def get_hole_right_indices():
    relative_column_start_index, relative_column_end_index = get_relative_column_indices()
    relative_row_start_index, relative_row_end_index = get_relative_row_indices()

    column_index = int(columns * relative_column_end_index)
    row_start_index = int(rows * relative_row_start_index)
    row_end_index = int(rows * relative_row_end_index)
    return column_index, row_start_index, row_end_index


def get_hole_top_indices():
    relative_column_start_index, relative_column_end_index = get_relative_column_indices()
    relative_row_start_index, relative_row_end_index = get_relative_row_indices()

    row_index = int(rows * relative_row_start_index)
    column_start_index = int(rows * relative_column_start_index)
    column_end_index = int(rows * relative_column_end_index)
    return row_index, column_start_index, column_end_index


def get_hole_bottom_indices():
    relative_column_start_index, relative_column_end_index = get_relative_column_indices()
    relative_row_start_index, relative_row_end_index = get_relative_row_indices()

    row_index = int(rows * relative_row_end_index)
    column_start_index = int(rows * relative_column_start_index)
    column_end_index = int(rows * relative_column_end_index)
    return row_index, column_start_index, column_end_index


def get_relative_column_indices():
    relative_column_start_index = (plate_height - hole_height) / (2.0 * plate_height)
    relative_column_end_index = (plate_height + hole_height) / (2.0 * plate_height)
    return relative_column_start_index, relative_column_end_index


def get_relative_row_indices():
    relative_row_start_index = (plate_width - hole_width) / (2.0 * plate_width)
    relative_row_end_index = (plate_width + hole_width) / (2.0 * plate_width)
    return relative_row_start_index, relative_row_end_index
