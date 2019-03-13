# This program will deal with the equation: Wrench = J^(T) * R * F_o * a
# Working with a 2joint,2link planar system
import sympy as sym
import numpy as np
from Symbolic_Matricies import J

expr = sym.sympify(J(2))


J = J(2).subs({'q_1': sym.rad(135), 'q_2': sym.rad(-120), 'l_1': 0.254, 'l_2': 0.305}).evalf().tolist()
J = np.array(J)
print(J)
