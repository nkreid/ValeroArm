# This function will find the largest circle in the FFS
import numpy as np


def LargestCircle(hull, x_center, y_center):
        space = np.linspace(0, 2*np.pi)
        circ = np.array([np.cos(space), np.sin(space)])
        r = 0
        step = 0.0005
        inHull = True


        while inHull == True:

            points = (r * circ) + np.array([[x_center], [y_center]])

            from scipy.spatial import Delaunay
            if not isinstance(hull,Delaunay):
                hull = Delaunay(hull)
            if np.all(hull.find_simplex(points.T)>=0):
                r += step
            else:
                break
        return r, points

