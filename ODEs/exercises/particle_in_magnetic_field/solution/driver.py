import numpy as np
from variables import *
from solver import *
from analyticsolver import *
from plotter import *

time_vector = np.zeros(n)
x_velocity_vector = np.zeros(n)
y_velocity_vector = np.zeros(n)

time_vector[0] = 0.0
x_velocity_vector[0] = vx_initial
y_velocity_vector[0] = vy_initial

for i in range(1, n):
    vx_updated, vy_updated = advance_iteration(x_velocity_vector[i-1], y_velocity_vector[i-1])

    x_velocity_vector[i] = vx_updated
    y_velocity_vector[i] = vy_updated
    time_vector[i] = h + time_vector[i-1]

analytic_x_velocity_vector = get_analytic_x_velocity(time_vector)
analytic_y_velocity_vector = get_analytic_y_velocity(time_vector)

plot_velocity(time_vector, x_velocity_vector, analytic_x_velocity_vector, "vx.png")
plot_velocity(time_vector, y_velocity_vector, analytic_y_velocity_vector, "vy.png")

print("Successful!")