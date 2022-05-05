# ---------------------- importing packages and modules ---------------------- #
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle, Rectangle
from animationdata import *

# ---------------------------- defining functions ---------------------------- #
def animate(index):
    animateGraph(index)
    animateShape(index)

def animateShape(index):
    ax1.clear()

    # adding the rod (rectangle from our POV)
    xRectangle = -lRod/2 + positionArray[index]
    yRectangle = R
    rod = Rectangle((xRectangle, yRectangle), lRod, 2*r)
    rod.set_facecolor(greenBlue)
    rod.set_edgecolor(greenBlue)
    ax1.add_patch(rod)

    # adding the cylinders (circles from our POV)
    firstCylinder = Circle((-l/2, 0), radius = R)
    secondCylinder = Circle((l/2, 0), radius = R)
    firstCylinder.set_facecolor(darkBlue)
    firstCylinder.set_edgecolor(darkBlue)
    secondCylinder.set_facecolor(darkBlue)
    secondCylinder.set_edgecolor(darkBlue)
    ax1.add_patch(firstCylinder)
    ax1.add_patch(secondCylinder)

    # making it so that the axes have equal number of pixels (so circles don't become ovals)
    ax1.axis("equal")

    # setting axes limits
    ax1.set_xlim(xmin = -3/4 * lRod, xmax = 3/4 * lRod)
    ax1.set_ylim(ymin = -1/6 * R, ymax = 1/4 * R)

    # displaying current time
    currentTime = timeArray[index]
    currentTimeFormattedString = "Time: " + "{0:.2f}".format(currentTime) + " s"
    ax1.set_title(currentTimeFormattedString)

    # hiding axes
    ax1.set_axis_off()


def animateGraph(index):
    ax2.clear()

    # adding base graph
    ax2.plot(timeArray, positionArray, color = darkBlue)
    ax2.set(xlabel = "Time (s)", ylabel = "Position (m)")
    ax2.grid()

    # adding a scatter point for the selected point
    ax2.scatter(timeArray[index], positionArray[index], color = greenBlue)

# -------------------------- getting animation data -------------------------- #
timeArray, positionArray = getAnimationData()

# ----------------------- setting animation properties ----------------------- #
intervalBetweenFrames = tEnd / n
framesPerSecond = 1 / intervalBetweenFrames
gifWriter = animation.PillowWriter(fps = framesPerSecond)
fileName = "result.gif"

# ---------------------------- creating animation ---------------------------- #
fig, (ax1, ax2) = plt.subplots(2, 1)
animatedPlot = animation.FuncAnimation(fig, animate, interval = intervalBetweenFrames, frames = n)

# ----------------------------- saving animation ----------------------------- #
animatedPlot.save(fileName, writer = gifWriter)