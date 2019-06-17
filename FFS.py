# This function will calculate and graph the feasible force set at a particular endpoint,
# with maximal endpoint activation and a fixed tendon routing configuration
# Working with a 2joint,2link planar system
import numpy as np
import matplotlib.pyplot as plt


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
        # Convert to Radians
        q_1 = np.radians(q1)

        J_square = np.array([l1*np.sin(q_1)])

        endpoint = np.array([[l_1*np.cos(q_1)], [l_1*np.sin(q_1)]])

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

    def LargestCircle(hul, x_center, y_center):
        space = np.linspace(0, 2*np.pi)
        circ = np.array([np.cos(space), np.sin(space)])
        r = 0
        step = 0.0005
        inHull = True

        while inHull == True:

            points = (r* circ) + np.array([x_center, y_center])

            from scipy.spatial import Delaunay
            if not isinstance(hul, Delaunay):
                hull = Delaunay(hul)
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
        plt.title('Feasible Forces with Elbow at ' + str(q2) + ' degrees')

        plt.show()

    return max_R


# l1 = .267
# l2 = .272
# r = np.array([[-1, -1, 1], [-1, 1, 0]])
# q2 = np.arange(10, 150, 10)
# rad = np.zeros((1, len(q2)))
# for i in range(len(q2)):
#     ffs(0, q2[i], l1, l2, r, 1, 'Y')
