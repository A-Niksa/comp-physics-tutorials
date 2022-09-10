import numpy as np
from config import *

def check_convergence(previousSum, newSum):
    return abs(newSum - previousSum) < tolerance

def get_sum_of_matrix(voltageMatrix):
    return np.sum(np.sum(voltageMatrix, axis = 1), axis = 0)