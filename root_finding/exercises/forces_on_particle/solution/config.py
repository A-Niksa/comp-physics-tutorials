# ----------------------- importing necessary packages ----------------------- #
import numpy as np

# ---------------- defining the equation in form of a function --------------- #
def eqn_function(r):
    return 2 * np.exp(0.75 * r) - r**3 + 5.5 * r

# ----------------------- defining the solver variables ---------------------- #
interval_1_start = 3
interval_1_end = 4

interval_2_start = 6
interval_2_end = 7

root_error = 1E-5
max_number_of_iterations = 10000