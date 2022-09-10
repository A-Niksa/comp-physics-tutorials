# ---------------------------- importing packages ---------------------------- #
from scipy.optimize import fsolve
from config.solverconfig import *

# ---------------------------- defining functions ---------------------------- #
def advance_iteration_by_backward_method(x_previous, z_previous):
    common_coefficient = 1 / (1 + alpha * h**2)
    x_updated = common_coefficient * (x_previous + h * z_previous)
    z_updated = common_coefficient * (z_previous - alpha * h * x_previous)
    return x_updated, z_updated