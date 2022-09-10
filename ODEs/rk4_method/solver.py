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
    constantTerm = (g * hole_area) / (delta * PI * r*r)
    return constantTerm * (height - x)

def advance_iteration(x_previous, z_previous, f, s):
    k0 = h * f(z_previous)
    l0 = h * s(x_previous, z_previous)
    k1 = h * f(z_previous + 0.5*l0)
    l1 = h * s(x_previous + 0.5*h, z_previous + 0.5*l0)
    k2 = h * f(x_previous + 0.5*h)
    l2 = h * s(x_previous + 0.5*h, z_previous + 0.5*l1)
    k3 = h * f(x_previous + h)
    l3 = h * s(x_previous + h, z_previous + l2)
    x_updated = x_previous + 1/6 * (k0 + 2*k1 + 2*k2 + k3)
    z_updated = z_previous + 1/6 * (l0 + 2*l1 + 2*l2 + l3)
    return x_updated, z_updated

# ---------------------------- physical variables ---------------------------- #
g = 9.81 # gravitational acceleration | m/s^2
hole_area = 3.14E-4 # hole area | m^2
delta = 1E-3 # container width | m
height = 0.2 # height of container | m
r = 0.25 # radius of bowl | m
PI = math.pi # pi number | 1

# --------------------------- ODE solvers variable --------------------------- #
h = 0.01 # increment
x_initial = 0 # initial height of water relative to base | m
z_initial = 0 # initial velocity through the hole | m/s

# ------------------------------ running solver ------------------------------ #
time_array = [0]
height_array =  [x_initial]
x_previous = x_initial
z_previous = z_initial
x_updated = 0
z_updated = 0
while (x_updated <= height):
    # advanding simulation by 1 iteration:
    x_updated, z_updated = advance_iteration(x_previous, z_previous, f, s)
    # storing the updated time and height:
    time_array.append(time_array[-1] + h)
    height_array.append(x_updated)
    # assigning updated values to the temporary value holders (xPrevious and zPrevious)
    x_previous = x_updated
    z_previous = z_updated

# ----------------------------- plotting results ----------------------------- #
plt.plot(time_array, height_array, color = "blue")
plt.xlabel("Time (s)")
plt.xlim(0, time_array[-1])
plt.ylabel("Height (m)")
plt.ylim(0, height_array[-1])
plt.title("Height Versus Time in the Saxon Bowl")
plt.grid(linestyle = '--')
plt.show()