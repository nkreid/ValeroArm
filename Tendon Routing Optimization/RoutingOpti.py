import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import itertools
from FFS import ffs

def optiFFS(rout):
    q2 = np.arange(1, 151, 1)
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


def poss_rows(value_list, length):
    row = np.array(list(itertools.product(value_list, repeat=length)))
    row_del = []
    for i in range(len(row)):
        if -1 in row[i] and 1 in row[i]:
            pass
        else:
            row_del.append(i)
    row = np.delete(row, row_del, 0)
    return row


# This function combines rows and removes matrices if they are
# different rearrangements of columns
def possible_routes(row1,row2):
    poss_list = []
    for i in row1:
        for j in row2:
            route = np.array([i, j])
            arr = route[:,np.lexsort((route[1,:], route[0,:]))]
            if not any((arr == x).all() for x in poss_list):
                poss_list.append(arr)
    return np.asarray(poss_list)

# There cant be a column the has a zero above a non-zero value this is because tendons
# can not pass a distal joint without first passing the ones proximal to it
a = poss_rows([-1, 1], 3)
b = poss_rows([-1, 0, 1], 3)

data = np.load('PossibleRoute.npy')
routes = []
radii = []
for i in data:
    try:
        f = optiFFS(i)
    except:
        f = 'Error'
    routes.append(i)
    radii.append(f)
print(routes)
print(radii)

