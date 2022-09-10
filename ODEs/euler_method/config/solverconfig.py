# ---------------------------- defining functions ---------------------------- #
def f(x, z):
    return z

def s(x, z):
    return -alpha * x

# ---------------------- system parameters and constants --------------------- #
g = 9.8 # gravitational acceleration | m/s^2
mu = 0.6 # kinetic friction coefficient
m = 0.5 # mass of the rod | kg
l = 1.5 # length between centres of the disks | m
alpha = 2 * g * mu / l

# --------------------------- ODE solvers variable --------------------------- #
h = 0.005 # increment
t_end = 20 # end of simulation | s
number_of_steps =  int(t_end / h) # number of steps
x_initial = 0.1 # initial height of water relative to base | m | added a small change relative to the centre
z_initial = 0 # initial velocity through the hole | m/s