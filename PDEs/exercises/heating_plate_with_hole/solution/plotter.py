# importing packages
from matplotlib import pyplot as plt
from matplotlib import cm


# the defining surface plotting function:
def plot_surface(x_matrix, y_matrix, nodes_matrix):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surface = ax.plot_surface(x_matrix, y_matrix, nodes_matrix, cmap=cm.coolwarm)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    cbar = fig.colorbar(surface)
    cbar.set_label("Temperature (K)")

    plt.savefig("result.png")
