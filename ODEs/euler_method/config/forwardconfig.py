# ---------------------------- importing functions --------------------------- #
from config.solverconfig import *

# ---------------------------- defining functions ---------------------------- #
def advance_iteration_by_forward_method(x_previous, z_previous):
    x_updated = x_previous + h * f(x_previous, z_previous)
    z_updated = z_previous + h * s(x_previous, z_previous)
    return x_updated, z_updated