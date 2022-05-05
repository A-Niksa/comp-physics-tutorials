# ---------------------------- importing packages ---------------------------- #
from config.solverconfig import *
from scipy.optimize import fsolve

# ---------------------------- defining functions ---------------------------- #
def advanceIterationByBackwardMethod(xPrevious, zPrevious):
    commonCoefficient = 1 / (1 + alpha * h**2)
    xUpdated = commonCoefficient * (xPrevious + h * zPrevious)
    zUpdated = commonCoefficient * (zPrevious - alpha * h * xPrevious)
    return xUpdated, zUpdated