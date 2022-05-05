# ---------------------------- importing libraries --------------------------- #
from matplotlib import pyplot as plt
from stability.energychecker import *
from stability.analyticsolution import *

# ---------------------------- defining functions ---------------------------- #
def plotResults(timeArray, positionArray, velocityArray, filePath):
    analyticPositionArray = calculateAnalyticResults(timeArray)
    energyArray = calculateTotalEnergy(positionArray, velocityArray)

    fig, (firstFigure, secondFigure) = plt.subplots(2, 1)

    firstFigure.plot(timeArray, positionArray, color = (0, 0, 0.55), label = "numerical")
    firstFigure.plot(timeArray, analyticPositionArray, color = (0, 0.25, 0.80), label = "analytic", linestyle = "dashed")
    firstFigure.legend(loc = "upper right")
    firstFigure.set(ylabel = "Position (m)")
    firstFigure.grid()

    secondFigure.plot(timeArray, energyArray, color = (0, 0, 0.55))
    secondFigure.set(xlabel = "Time (s)", ylabel = "Total Energy (J)")
    minimumY, maximumY = calculateEnergyYLimits()
    secondFigure.set_ylim([minimumY, maximumY])
    secondFigure.grid()

    fig.savefig(filePath)

def calculateEnergyYLimits():
    maximumY = 1.5 * alpha * m * xInitial ** 2 # 3 * (1/2 * k * A^2) = 3 * Emax as seen in simple harmanic motion
    return 0, maximumY