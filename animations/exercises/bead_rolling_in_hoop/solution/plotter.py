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

    # adding the bead (solid circle from our POV)
    x_bead = x_position_array[index]
    y_bead = y_position_array[index]
    bead = Circle((x_bead, y_bead), radius = r)
    bead.set_facecolor(green_blue)
    bead.set_edgecolor(green_blue)
    ax1.add_patch(bead)

    # adding the hoop (hollow circle from our POV)
    hoop = Circle((0, 0), radius = R)
    hoop.set_edgecolor(dark_blue)
    hoop.set_facecolor("None")
    ax1.add_patch(hoop)

    # making it so that the axes have equal number of pixels (so circles don't become ovals)
    ax1.axis("equal")

    # setting axes limits
    ax1.set_xlim(xmin = -R, xmax = R)
    ax1.set_ylim(ymin = -R, ymax = R)

    # displaying current time
    current_time = time_array[index]
    current_time_formatted_string = "Time: " + "{0:.2f}".format(current_time) + " s"
    ax1.set_title(current_time_formatted_string)

    # hiding axes
    ax1.set_axis_off()


def animate_graph(index):
    ax2.clear()

    # adding base graph
    ax2.plot(time_array, angle_array, color = dark_blue)
    ax2.set(xlabel = "Time (s)", ylabel = "Angle (rad)")
    ax2.grid()

    # adding a scatter point for the selected point
    ax2.scatter(time_array[index], angle_array[index], color = green_blue)

# -------------------------- getting animation data -------------------------- #
time_array, angle_array, x_position_array, y_position_array = get_animation_data()

# ----------------------- setting animation properties ----------------------- #
interval_between_frames = t_end / n
frames_per_second = 1 / interval_between_frames
gif_writer = animation.PillowWriter(fps = frames_per_second)
file_name = "result.gif"

# ---------------------------- creating animation ---------------------------- #
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (5, 6), gridspec_kw={'height_ratios': [2, 1]})
animated_plot = animation.FuncAnimation(fig, animate, interval = interval_between_frames, frames = n)

# ----------------------------- saving animation ----------------------------- #
animated_plot.save(file_name, writer = gif_writer, dpi = 300)