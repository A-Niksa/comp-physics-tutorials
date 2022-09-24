# -------------------------- importing numpy for pi -------------------------- #
import numpy as np

# ------------------ defining system variables and constants ----------------- #
theta_initial = np.pi/4 # starting angle of the bead | rad
g = 9.81 # gravitational acceleration | m/s^2
m = 0.0315 # mass of the bead | kg
R = 0.125 # hoop radius | m
r = 0.015 # bead radius | m

t_end = 20 # end time of the simulation | s
n = 500 # number of time points

# ------------------------------ defining colors ----------------------------- #
dark_blue = (0, 0.1, 0.5)
green_blue = (0, 0.55, 0.6)