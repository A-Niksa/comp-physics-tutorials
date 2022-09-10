# ---------------------------- importing functions --------------------------- #
from config.solverconfig import *

# ---------------------------- defining functions ---------------------------- #
def advance_iteration_by_symplectic_method(x_previous, z_previous):
    x_updated = x_previous + h * z_previous
    z_updated = z_previous - h * alpha * x_updated
    return x_updated, z_updated