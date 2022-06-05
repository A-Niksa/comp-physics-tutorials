import numpy as np
from config import *

def checkConvergence(voltageMatrix, previousSum, newSum):
    return abs(newSum - previousSum) < tolerance

def getSumOfMatrix(voltageMatrix):
    return np.sum(np.sum(voltageMatrix, axis = 1), axis = 0)