# ---------------------------- importing packages ---------------------------- #
from config.solverconfig import *
from plotting.plotter import *
from config.forwardconfig import *
from config.backwardconfig import *
from config.symplecticconfig import *
import numpy as np

# -------------------------- choosing solver method and path ----------------- #
print("Please choose one of these approaches:\n1) Forward Euler Method\n" + \
    "2) Backward Euler Method\n3) Symplectic Euler Method")
solverMethod = int(input())
filePath = "plotting/results/"
match solverMethod:
    case 1:
        advanceIteration = advanceIterationByForwardMethod
        filePath += "forwardresults.png"
    case 2:
        advanceIteration = advanceIterationByBackwardMethod
        filePath += "backwardresults.png"
    case 3:
        advanceIteration = advanceIterationBySymplecticMethod
        filePath += "symplecticresults.png"

# ------------------------------ running solver ------------------------------ #
timeArray = np.zeros(numberOfSteps)
positionArray =  np.zeros(numberOfSteps)
positionArray[0] = xInitial
velocityArray = np.zeros(numberOfSteps)
velocityArray[0] = zInitial
xPrevious = xInitial
zPrevious = zInitial
xUpdated = 0
zUpdated = 0
for i in range(1, numberOfSteps):
    # getting the (i-1)th values
    xPrevious = positionArray[i-1]
    zPrevious = velocityArray[i-1]

    # calculating new values of x and z
    xUpdated, zUpdated = advanceIteration(xPrevious, zPrevious)

    # storing new values of x and z
    timeArray[i] = timeArray[i-1] + h
    positionArray[i] = xUpdated
    velocityArray[i] = zUpdated

# --------------------------- plotting the results --------------------------- #
plotResults(timeArray, positionArray, velocityArray, filePath)