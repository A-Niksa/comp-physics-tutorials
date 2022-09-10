from variables import *
import numpy as np

def get_analytic_x_velocity(time_vector):
    analytic_x_velocity = np.sqrt(2) * vx_initial * np.sin(3.14/4 + omega * time_vector)
    return analytic_x_velocity

def get_analytic_y_velocity(time_vector):
    analytic_y_velocity = np.sqrt(2) * vy_initial * np.cos(3.14/4 + omega * time_vector)
    return analytic_y_velocity