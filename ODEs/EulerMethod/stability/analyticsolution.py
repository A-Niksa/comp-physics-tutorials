# ------------------------ importing necessary modules ----------------------- #
from config.solverconfig import *
import numpy as np
import math

# ---------------------------- defining functions ---------------------------- #
def calculateAnalyticResults(timeArray):
    angularFrequency = math.sqrt(2 * g * mu / l)
    analyticPositionArray = np.zeros(numberOfSteps)
    for i in range(numberOfSteps):
        analyticPositionArray[i] = xInitial * math.cos(angularFrequency * timeArray[i])
    
    return analyticPositionArray