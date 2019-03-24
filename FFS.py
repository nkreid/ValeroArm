# This function will calcualte and graph the feasible force set at a particular endpoint,
# with maximal endpoint activation and a fixed tendon routing configuration
# Working with a 2joint,2link planar system
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from Symbolic_Matricies import J, T_0_to


def ffs(q_1, q_2, l_1, l_2, R, maxmotorforce):

    # Endpoint of limb
    endpoint_list = T_0_to(2).subs({'q_1': sym.rad(q_1), 'q_2': sym.rad(q_2), 'l_1': l_1 , 'l_2': l_2}).evalf().tolist()
    endpoint = np.array(endpoint_list, dtype= 'float')[:2,3]

    # Creating the numerical Jacobian for the system J(2) is for a 2 joint, 2 link system
    J_num = J(2).subs({'q_1': sym.rad(q_1), 'q_2': sym.rad(q_2), 'l_1': l_1 , 'l_2': l_2}).evalf().tolist()
    J_mat = np.array(J_num, dtype='float')
    J_square = J_mat[:2, :2] # Reduce the Jacobian to a square matrix

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


    W = np.zeros((2,8))
    for i in range(len(a_poss)):
        W[:,i] = H.dot(a_poss[i].T)
    hull = ConvexHull(W.T)

    # Graphing of FFS
    plt.plot(W[0],W[1], 'bo') # maximal forces are blue
    plt.plot(endpoint[0], endpoint[1], 'ro') # endpoint is red
    for simplex in hull.simplices:
        plt.plot(W.T[simplex, 0], W.T[simplex, 1], 'k-')

    # Graph Formatting
    plt.xlabel('Force in X-Direction')
    plt.ylabel('Force in Y-Direction')
    plt.title('Feasible Forces at a Fixed Endpoint')

    plt.show()

r = np.array([[-1, 1, -1], [1, 0, -1]])
ffs(135, -120, .254, .305, r, 1)



