import numpy as np
from variables import *
from solver import *
from analyticsolver import *
from plotter import *

timeVector = np.zeros(n)
xVelocityVector = np.zeros(n)
yVelocityVector = np.zeros(n)

timeVector[0] = 0.0
xVelocityVector[0] = vxInitial
yVelocityVector[0] = vyInitial

for i in range(1, n):
    vxUpdated, vyUpdated = advanceIteration(xVelocityVector[i-1], yVelocityVector[i-1])

    xVelocityVector[i] = vxUpdated
    yVelocityVector[i] = vyUpdated
    timeVector[i] = h + timeVector[i-1]

xAnalyticVelocityVector = getXAnalyticVelocity(timeVector)
yAnalyticVelocityVector = getYAnalyticVelocity(timeVector)

plotVelocity(timeVector, xVelocityVector, xAnalyticVelocityVector, "vx.png")
plotVelocity(timeVector, yVelocityVector, yAnalyticVelocityVector, "vy.png")

print("Successful!")