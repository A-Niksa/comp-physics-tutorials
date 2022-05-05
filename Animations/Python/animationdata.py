# ---------------------------- importing packages ---------------------------- #
import numpy as np
from config import *

# ---------------------------- defining functions ---------------------------- #
def getAnimationData():
    timeArray = np.linspace(0, tEnd, n)

    angularFrequency = np.sqrt(2 * g * mu / l)
    positionArray = xInitial * np.cos(angularFrequency * timeArray)

    return timeArray, positionArray