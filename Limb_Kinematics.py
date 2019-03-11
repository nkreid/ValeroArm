import numpy as np


def rotate(axis, angle):
    R = np.eye(3, 3)
    if axis == 'k':
        R[0, 0] = np.cos(angle)
        R[1, 1] = np.cos(angle)
        R[1, 0] = np.sin(angle)
        R[0, 1] = -1*np.sin(angle)
    elif axis == 'j':
        R[0, 0] = np.cos(angle)
        R[2, 2] = np.cos(angle)
        R[0, 2] = np.sin(angle)
        R[2, 0] = -1*np.sin(angle)
    elif axis == 'i':
        R[2, 2] = np.cos(angle)
        R[1, 1] = np.cos(angle)
        R[2, 1] = np.sin(angle)
        R[1, 2] = -1*np.sin(angle)
    else:
        print('Not a valid rotation axis')
    return R


def transform(rotation, translation):
    T = np.eye(4, 4)
    T[0:3, 0:3] = rotation
    T[0:3, 3] = translation
    return T


def geometric(T, *angles):
    x = T[0, 3]
    y = T[1, 3]
    alpha = 0
    for angle in angles:
        alpha += angle
    G = np.array([[x], [y], [alpha]])
    return G
