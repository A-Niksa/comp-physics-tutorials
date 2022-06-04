from variables import *
import numpy as np

def getXAnalyticVelocity(timeVector):
    xAnalyticVelocity = np.sqrt(2) * vxInitial * np.sin(3.14/4 + omega * timeVector)
    return xAnalyticVelocity

def getYAnalyticVelocity(timeVector):
    yAnalyticVelocity = np.sqrt(2) * vyInitial * np.cos(3.14/4 + omega * timeVector)
    return yAnalyticVelocity