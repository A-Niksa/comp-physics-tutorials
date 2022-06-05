from config import *

def computeWeightedAverage(voltageMatrix, i, j):
    computedAverage = 1 / (2 * (hx*hx + hy*hy)) * \
        (hx*hx * (voltageMatrix[i, j+1] + voltageMatrix[i, j-1]) + \
            hy*hy * (voltageMatrix[i+1, j] + voltageMatrix[i-1, j]))

    return computedAverage