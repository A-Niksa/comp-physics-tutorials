# ---------------------------- importing functions --------------------------- #
from config.solverconfig import *

# ---------------------------- defining functions ---------------------------- #
def advanceIterationByForwardMethod(xPrevious, zPrevious):
    xUpdated = xPrevious + h * f(xPrevious, zPrevious)
    zUpdated = zPrevious + h * s(xPrevious, zPrevious)
    return xUpdated, zUpdated