from variables import *

def advanceIteration(vxPrevious, vyPrevious):
    vxUpdated = vxPrevious + h * f(vxPrevious, vyPrevious)
    vyUpdated = vyPrevious + h * g(vxPrevious, vyPrevious)

    return vxUpdated, vyUpdated

def f(vxPrevious, vyPrevious):
    return omega * vyPrevious

def g(vxPrevious, vyPrevious):
    return -omega * vxPrevious