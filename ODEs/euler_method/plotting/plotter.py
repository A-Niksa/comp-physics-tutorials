# ---------------------------- importing libraries --------------------------- #
from matplotlib import pyplot as plt
from stability.energychecker import *
from stability.analyticsolution import *

# ---------------------------- defining functions ---------------------------- #
def plot_results(time_array, position_array, velocity_array, file_path):
    analytic_position_array = calculate_analyitic_results(time_array)
    energyArray = calculate_total_energy(position_array, velocity_array)

    fig, (first_fig, second_fig) = plt.subplots(2, 1)

    first_fig.plot(time_array, position_array, color = (0, 0, 0.55), label = "numerical")
    first_fig.plot(time_array, analytic_position_array, color = (0, 0.25, 0.80), label = "analytic", linestyle = "dashed")
    first_fig.legend(loc = "upper right")
    first_fig.set(ylabel = "Position (m)")
    first_fig.grid()

    second_fig.plot(time_array, energyArray, color = (0, 0, 0.55))
    second_fig.set(xlabel = "Time (s)", ylabel = "Total Energy (J)")
    minimum_y, maximum_y = calculate_energy_y_limits()
    second_fig.set_ylim([minimum_y, maximum_y])
    second_fig.grid()

    fig.savefig(file_path)

def calculate_energy_y_limits():
    maximum_y = 1.5 * alpha * m * x_initial ** 2 # 3 * (1/2 * k * A^2) = 3 * Emax as seen in simple harmanic motion
    return 0, maximum_y