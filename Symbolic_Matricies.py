# This file will take the number of DOFs (joints) and output symbolic matrices for G and J
# in 2D, we can assume number of joints equals number of links
# this model works for n+1 muslces, assuming n joints
import sympy as sym
from sympy.printing.str import StrPrinter as StrPrinter #for formating matrix outputs


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
    for i in range(n+1):
        if i != n:
            T *= T_n(i)
        else:
            l_n = sym.symbols('l_'+str(n))
            x = sym.eye(4,4)
            x[0, 3] = l_n
            T *= x
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


def r(joints, muscles):
    r = sym.zeros(joints, muscles)
    for i in range(joints):
        for j in range(muscles):
            r_ij = sym.symbols('r_' + str(i+1)+str(j+1))
            r[i, j] = r_ij
    return r


def f(muscles):
    f = sym.eye(muscles, muscles)
    for i in range(muscles):
        f_i = sym.symbols('f_' + str(i+1))
        f[i, i] = f_i
    return f


def a(muscles):
    a = sym.ones(muscles, 1)
    for i in range(muscles):
        a_i = sym.symbols('a_' + str(i+1))
        a[i, 0] = a_i
    return a


def end_f(joints, muscles):
    Jtrans = J(joints).T
    Jtrans.col_del(-1)  # deleting last row to remove dependent vars if not square
    return Jtrans**(-1) * r(joints, muscles) * f(muscles) * a(muscles)



# A.table(StrPrinter()) or for Matrix layout
# A.tolist() for list to


