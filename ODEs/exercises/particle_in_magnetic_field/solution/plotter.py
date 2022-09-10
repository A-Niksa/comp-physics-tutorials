from matplotlib import pyplot as plt
from variables import *

def plot_velocity(time_vector, velocity_vector, analytic_velocity_vector, file_name):
    plt.plot(time_vector, velocity_vector, label = "numerical")
    plt.plot(time_vector, analytic_velocity_vector, label = "analytic")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.legend(loc = "upper left")
    plt.grid()

    plt.savefig(file_name)
    plt.close()