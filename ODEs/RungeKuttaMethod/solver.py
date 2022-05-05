# CaYPT Committee
# Student Resources Team
# By: Arsha Niksa
# Computational Physics Tutorial
# Topic: Solving an ODE
# Sample Problem: Saxon Bowl (Problem 6 | 2020)

# ------------------------ importing required packages ----------------------- #
import math
import matplotlib.pyplot as plt

# ----------------------- defining necessary functions ----------------------- #
def f(z):
    return z

def s(x, z):
    constantTerm = (g * S) / (delta * PI * r*r)
    return constantTerm * (height - x)

def advanceIteration(xPrevious, zPrevious, f, s):
    k0 = h * f(zPrevious)
    l0 = h * s(xPrevious, zPrevious)
    k1 = h * f(zPrevious + 0.5 * l0)
    l1 = h * s(xPrevious + 0.5 * h, zPrevious + 0.5 * l0)
    k2 = h * f(xPrevious + 0.5 * h)
    l2 = h * s(xPrevious + 0.5 * h, zPrevious + 0.5 * l1)
    k3 = h * f(xPrevious + h)
    l3 = h * s(xPrevious + h, zPrevious + l2)
    xUpdated = xPrevious + 1/6 * (k0 + 2*k1 + 2*k2 + k3)
    zUpdated = zPrevious + 1/6 * (l0 + 2*l1 + 2*l2 + l3)
    return xUpdated, zUpdated

# ---------------------------- physical variables ---------------------------- #
g = 9.81 # gravitational acceleration | m/s^2
S = 3.14E-4 # hole area | m^2
delta = 1E-3 # container width | m
height = 0.2 # height of container | m
r = 0.25 # radius of bowl | m
PI = math.pi # pi number | 1

# --------------------------- ODE solvers variable --------------------------- #
h = 0.01 # increment
xInitial = 0 # initial height of water relative to base | m
zInitial = 0 # initial velocity through the hole | m/s

# ------------------------------ running solver ------------------------------ #
timeArray = [0]
heightArray =  [xInitial]
xPrevious = xInitial
zPrevious = zInitial
xUpdated = 0
zUpdated = 0
while (xUpdated <= height):
    # advanding simulation by 1 iteration:
    xUpdated, zUpdated = advanceIteration(xPrevious, zPrevious, f, s)
    # storing the updated time and height:
    timeArray.append(timeArray[-1] + h)
    heightArray.append(xUpdated)
    # assigning updated values to the temporary value holders (xPrevious and zPrevious)
    xPrevious = xUpdated
    zPrevious = zUpdated

# ----------------------------- plotting results ----------------------------- #
plt.plot(timeArray, heightArray, color = "blue")
plt.xlabel("Time (s)")
plt.xlim(0, timeArray[-1])
plt.ylabel("Height (m)")
plt.ylim(0, heightArray[-1])
plt.title("Height Versus Time in the Saxon Bowl")
plt.grid(linestyle = '--')
plt.show()