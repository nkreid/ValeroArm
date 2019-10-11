from FFS import ffs
import numpy as np
from scipy import integrate


def optiFFS(rout):
    q2 = np.arange(1, 151, 20)
    l1 = .267
    l2 = .272
    rad = np.zeros((1, len(q2)))
    for i in range(len(q2)):
            rad[0, i] = ffs(0, q2[i], l1, l2, rout, 1)
    area = integrate.trapz(np.absolute(rad), x=q2)
    return float(area)


# This function shows a graph that shows there is no dependence of the shoulder angle
# on the optimization parameter


def optiplot(rout):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    q1 = np.linspace(-40, 170, 15)
    q2 = np.linspace(-10, 150, 15)
    l1 = .267
    l2 = .272
    rad = np.zeros((len(q1), len(q2)))
    for i in range(len(q1)):
        for e in range(len(q2)):
            rad[i, e] = ffs(q1[i], q2[e], l1, l2, rout, 1)


    q1, q2 = np.meshgrid(q1, q2)
    ax.plot_surface(q1, q2, rad, linewidth=0, antialiased=False)

    # Plot formatting
    plt.xlabel('Shoulder Angle')
    plt.ylabel('Elbow Angle')
    plt.title('Max radius at given endpoint')
    plt.xlim(-40, 170)
    plt.ylim(-10, 150)
    plt.show()

