import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import itertools

#
def ffs(q1, q2, l_1, l_2, R, maxmotorforce, plotOn = 'N'):


    if q2 != 0:

        # Convert to Radians
        q_1 = np.radians(q1)
        q_2 = np.radians(q2)

        # Endpoint of limb
        endpoint = np.array([[l_1*np.cos(q_1) + l_2*np.cos(q_1 + q_2)], [l_1*np.sin(q_1) + l_2*np.sin(q_1 + q_2)]])

        # Creating the numerical Jacobian for the system J(2) is for a 2 joint, 2 link system
        J_mat = np.array([[-l_1 * np.sin(q_1) - l_2*np.sin(q_1 + q_2), -l_2*np.sin(q_1 + q_2)],
                          [l_1*np.cos(q_1) + l_2*np.cos(q_1 + q_2),  l_2*np.cos(q_1 + q_2)],
                          [1, 1]])
        J_square = J_mat[:2, :2] # Reduce the Jacobian to a square matrix

    else:
        pass # Come back to this later, we have to deal when the elbow crosses zero

    # Creating Inverse Transpose of the Jacobian
    J_inv = np.linalg.inv(J_square)
    J_inv_T = J_inv.T

    # Max muscle force matrix
    F_0 = np.diag([maxmotorforce, maxmotorforce, maxmotorforce])

    # H matrix
    H = J_inv_T.dot(R).dot(F_0)

    # Muscle activation possibilities
    a_poss = np.array([[1, 1, 1],
                       [1, 0, 0],
                       [1, 0, 1],
                       [1, 1, 0],
                       [0, 1, 1],
                       [0, 1, 0],
                       [0, 0, 1],
                       [0, 0, 0]])

    from scipy.spatial import ConvexHull
    W = np.zeros((2,8))
    for i in range(len(a_poss)):
        W[:,i] = H.dot(a_poss[i].T)
    hull = ConvexHull(W.T)

    def LargestCircle(hull, x_center, y_center):
        space = np.linspace(0, 2*np.pi)
        circ = np.array([np.cos(space), np.sin(space)])
        r = 0
        step = 0.0005
        inHull = True

        while inHull == True:

            points = (r* circ) + np.array([x_center, y_center])

            from scipy.spatial import Delaunay
            if not isinstance(hull,Delaunay):
                hull = Delaunay(hull)
            if np.all(hull.find_simplex(points.T)>=0):
                r += step
            else:
                break
        return r, points

    max_R, circle = LargestCircle(W.T, endpoint[0], endpoint[1])

    # Graphing of FFS
    if plotOn == 'Y':
        plt.plot(W[0], W[1], 'bo') # maximal forces are blue
        plt.plot(endpoint[0], endpoint[1], 'ro') # endpoint is red
        plt.plot(circle[0], circle[1], 'g-')
        for simplex in hull.simplices:
            plt.plot(W.T[simplex, 0], W.T[simplex, 1], 'k-')

        # Graph Formatting
        plt.xlabel('Force in X-Direction')
        plt.ylabel('Force in Y-Direction')
        plt.title('Feasible Forces at a Fixed Endpoint')

        plt.show()

    return max_R


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
dicts = dict(zip(routes, radii))
print(dicts)

