# ---------------------------- importing packages ---------------------------- #
import numpy as np
from config import *
from solver import *
from convergence import *
from plotter import *

# ---------------------- initializing the voltage matrix --------------------- #
voltageMatrix = np.zeros((rows, columns))
voltageMatrix[:, 0] = np.ones(rows) * leftVoltage
voltageMatrix[:, columns - 1] = np.ones(rows) * rightVoltage
voltageMatrix[0, :] = np.ones(columns) * topVoltage
voltageMatrix[rows - 1, :] = np.ones(columns) * bottomVoltage

# -------------------------- iterating over the grid ------------------------- #
previousSum = 0
newSum = tolerance * 10
while not checkConvergence(voltageMatrix, previousSum, newSum):
    for i in range(1, rows-1):
        for j in range(1, columns-1):
            voltageMatrix[i, j] = computeWeightedAverage(voltageMatrix, i, j)
    
    previousSum = newSum
    newSum = getSumOfMatrix(voltageMatrix)

    print("current error: " + str(abs(newSum - previousSum)))

# --------------------------- plotting the results --------------------------- #
X = np.arange(0, height, hx)
Y = np.arange(0, width, hy)
X, Y = np.meshgrid(X, Y)
plotSurface(X, Y, voltageMatrix)

print("SUCCESS!")