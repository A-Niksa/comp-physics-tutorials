from variables import *

def advance_iteration(vx_previous, vy_previous):
    vx_updated = vx_previous + h * f(vy_previous)
    vy_updated = vy_previous + h * g(vx_previous)

    return vx_updated, vy_updated

def f(vy_previous):
    return omega * vy_previous

def g(vx_previous):
    return -omega * vx_previous