# ---------------------------- importing functions --------------------------- #
from config.solverconfig import *

# ---------------------------- defining functions ---------------------------- #
def advanceIterationBySymplecticMethod(xPrevious, zPrevious):
    xUpdated = xPrevious + h * zPrevious
    zUpdated = zPrevious - h * alpha * xUpdated
    return xUpdated, zUpdated