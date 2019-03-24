# This program will deal with the equation: Wrench = J^(T) * R * F_o * a
# Working with a 2joint,2link planar system
import sympy as sym
import numpy as np
from Symbolic_Matricies import J

expr = sym.sympify(J(2))



def ffs(q_1, q_2, l_1, l_2, R, maxmotorforce):

    # Creating the numerical Jacobian for the system J(2) is for a 2 joint, 2 link system
    J_num = J(2).subs({'q_1': sym.rad(q_1), 'q_2': sym.rad(q_2), 'l_1': l_1 , 'l_2': l_2}).evalf().tolist()
    J_mat = np.array(J_num, dtype= 'float')
    J_square = J_mat[:2, :2] # Reduce the Jacobian to a square matrix

    # Creating Inverse Transpose of the Jacobian
    J_inv = np.linalg.inv(J_square)
    J_inv_T = J_inv.T
    print(J_inv_T)


ffs(135, -50, .234, .23562, 1, 1)


