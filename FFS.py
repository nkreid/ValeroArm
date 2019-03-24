# This program will deal with the equation: Wrench = J^(T) * R * F_o * a
# Working with a 2joint,2link planar system
import sympy as sym
import numpy as np
import matplotlib as plt
from Symbolic_Matricies import J

r = np.array([[-1, 1, -1], [1, 0, -1]])


def ffs(q_1, q_2, l_1, l_2, R, maxmotorforce):

    # Creating the numerical Jacobian for the system J(2) is for a 2 joint, 2 link system
    J_num = J(2).subs({'q_1': sym.rad(q_1), 'q_2': sym.rad(q_2), 'l_1': l_1 , 'l_2': l_2}).evalf().tolist()
    J_mat = np.array(J_num, dtype= 'float')
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

    # Minkowski sum
    W = np.zeros((2,8))
    for i in range(len(a_poss)):
        W[:,i] = H.dot(a_poss[i].T)
    f_x = W[0]
    f_y = W[1]


ffs(1,1,1,1,r,3)



