# ---------------------- importing packages and modules ---------------------- #
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle, Rectangle
from animationdata import *

# ---------------------------- defining functions ---------------------------- #
def animate(index):
    animate_graph(index)
    animate_shape(index)

def animate_shape(index):
    ax1.clear()

    # adding the rod (rectangle from our POV)
    x_rectangle = -l_rod/2 + position_array[index]
    y_rectangle = R
    rod = Rectangle((x_rectangle, y_rectangle), l_rod, 2*r)
    rod.set_facecolor(green_blue)
    rod.set_edgecolor(green_blue)
    ax1.add_patch(rod)

    # adding the cylinders (circles from our POV)
    first_cylinder = Circle((-l/2, 0), radius = R)
    second_cylinder = Circle((l/2, 0), radius = R)
    first_cylinder.set_facecolor(dark_blue)
    first_cylinder.set_edgecolor(dark_blue)
    second_cylinder.set_facecolor(dark_blue)
    second_cylinder.set_edgecolor(dark_blue)
    ax1.add_patch(first_cylinder)
    ax1.add_patch(second_cylinder)

    # making it so that the axes have equal number of pixels (so circles don't become ovals)
    ax1.axis("equal")

    # setting axes limits
    ax1.set_xlim(xmin = -3/4 * l_rod, xmax = 3/4 * l_rod)
    ax1.set_ylim(ymin = -1/6 * R, ymax = 1/4 * R)

    # displaying current time
    current_time = time_array[index]
    current_time_formatted_string = "Time: " + "{0:.2f}".format(current_time) + " s"
    ax1.set_title(current_time_formatted_string)

    # hiding axes
    ax1.set_axis_off()


def animate_graph(index):
    ax2.clear()

    # adding base graph
    ax2.plot(time_array, position_array, color = dark_blue)
    ax2.set(xlabel = "Time (s)", ylabel = "Position (m)")
    ax2.grid()

    # adding a scatter point for the selected point
    ax2.scatter(time_array[index], position_array[index], color = green_blue)

# -------------------------- getting animation data -------------------------- #
time_array, position_array = get_animation_data()

# ----------------------- setting animation properties ----------------------- #
interval_between_frames = t_end / n
frames_per_second = 1 / interval_between_frames
gif_writer = animation.PillowWriter(fps = frames_per_second)
file_name = "result.gif"

# ---------------------------- creating animation ---------------------------- #
fig, (ax1, ax2) = plt.subplots(2, 1)
animated_plot = animation.FuncAnimation(fig, animate, interval = interval_between_frames, frames = n)

# ----------------------------- saving animation ----------------------------- #
animated_plot.save(file_name, writer = gif_writer)