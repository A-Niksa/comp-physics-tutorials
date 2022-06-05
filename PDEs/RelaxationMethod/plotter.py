from matplotlib import pyplot as plt
from matplotlib import cm

def plotSurface(X, Y, voltageMatrix):
    fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})
    surface = ax.plot_surface(X, Y, voltageMatrix, cmap = cm.coolwarm)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("z (m)")
    cbar = fig.colorbar(surface)
    cbar.set_label("Voltage (V)")

    plt.savefig("result.png")
