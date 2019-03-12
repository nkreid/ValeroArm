# This file will take the number of links and the number of DOFs and output symbolic matrices
import sympy as sym
from sympy.printing.str import StrPrinter as StrPrinter
# in 2D, we can assume # of links is always one more than # of joints (no joint at end of last link)


def R_n(n):
    q_n = sym.symbols('q_'+str(n+1))
    R = sym.eye(3)
    R[0, 0] = sym.cos(q_n)
    R[1, 1] = sym.cos(q_n)
    R[1, 0] = sym.sin(q_n)
    R[0, 1] = -1*sym.sin(q_n)
    return R


def T_n(n):
    # n is defined as the state the transform is going to from n+1
    l_n = sym.symbols('l_'+str(n))
    T = sym.eye(4, 4)
    T[0:3, 0:3] = R_n(n)
    if n != 0:
        T[0, 3] = l_n
    return T


def T_0_to(n):
    # this function dots the T_n matrices from 0 to n-1
    T = 1
    for i in range(n):
        T *= T_n(i)
    return sym.trigsimp(T)  # sym.trigsimp() uses trig identities to simplify the matrix


def G(joints):
    n = joints
    x = T_0_to(n+1)[0, 3]
    y = T_0_to(n+1)[1, 3]
    alpha = 0
    for i in range(n):
        q_i = sym.symbols('q_'+str(i+1))
        alpha += q_i
    G = sym.Matrix([[x], [y], [alpha]])
    return G


def J(joints):
    X = G(joints)
    Q = []
    for i in range(joints):
        q_i = sym.symbols('q_' + str(i+1))
        Q.append(q_i)
    return X.jacobian(Q)

# print A.table(StrPrinter()) for Matrix layout

# B = sym.trigsimp(T_n(0)*T_n(1)*T_n(2))
# print(B.table(StrPrinter()))
# C = T_0_to(3)
# print(C.table(StrPrinter()))

x = int(input('How many joints are in the system?'))
print('The G matrix is')
print(G(x).table(StrPrinter()))
print('\nThe J matrix is')
print(J(x).table(StrPrinter()))
