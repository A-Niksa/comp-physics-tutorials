# ---------------------------- importing packages ---------------------------- #
from turtle import position
from config.solverconfig import *
import numpy as np

# ---------------------------- defining functions ---------------------------- #
def calculateTotalEnergy(positionArray, velocityArray):
    energyArray = np.zeros(len(positionArray))
    for i in range(len(positionArray)):
        calculatedKineticEnergy = 0.5 * m * velocityArray[i] ** 2
        calculatedPotentialEnergy = 0.5 * alpha * m * positionArray[i] ** 2
        energyArray[i] = calculatedKineticEnergy + calculatedPotentialEnergy

    return energyArray  