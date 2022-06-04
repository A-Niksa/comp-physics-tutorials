from matplotlib import pyplot as plt
from variables import *

def plotVelocity(timeVector, velocityVector, analyticVelocityVector, fileName):
    plt.plot(timeVector, velocityVector, label = "numerical")
    plt.plot(timeVector, analyticVelocityVector, label = "analytic")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.legend(loc = "upper left")
    plt.grid()

    plt.savefig(fileName)
    plt.close()