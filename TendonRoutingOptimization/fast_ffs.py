import numpy as np
import time
from scipy.spatial import Delaunay
from FFS import ffs

def fast_ffs(q2, R):

	# Convert to Radians
	q_2 = np.radians(q2)
	sin = np.sin(q_2)
	cos = np.cos(q_2)

	# Endpoint of limb
	endpoint = np.array([[.267 + .272 * cos], [ .272 * sin]])

	# Jacobian for the system for a 2 joint, 2 link system, fixed length, shoulder at zero
	J_mat = np.array([[- .272*sin, -.272*sin],
					  [.267 + .272*cos,  .272*cos]])

	# Creating Inverse Transpose of the Jacobian
	determ = (1/0.272)*(1/((-.272*sin*cos)+(sin*(.267+.272*cos))))
	J_inv_T = np.array([determ]) * np.array([[.272*cos, -.267 - .272*cos], [.272*sin, -.272*sin]])
	# Max muscle force matrix
	F_0 = np.diag([1, 1, 1])

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
		bounds_of_radius = [0.0,10.0]
		inHull = True
		tolerance = 0.0001
		num_iterations = 0

		while inHull == True:

			if bounds_of_radius[1] - bounds_of_radius[0] < tolerance:
				# print("%s iter, final_radius: %s , route: %s "%(num_iterations, bounds_of_radius[1], R))
				return(bounds_of_radius[1],points)

			r = (bounds_of_radius[0] + bounds_of_radius[1])/2.0
			points = (r * circ) + np.array([x_center, y_center])

			if not isinstance(hul, Delaunay):
				hull = Delaunay(hul)

			was_too_small = np.all(hull.find_simplex(points.T) >= 0)
			num_iterations += 1
			if was_too_small:
				bounds_of_radius = [r, bounds_of_radius[1]]
			else:
				bounds_of_radius = [bounds_of_radius[0], r]
	max_R, circle = LargestCircle(W.T, endpoint[0], endpoint[1])
		
	return max_R

# start_time2 = time.time()
# r = np.array([[-1, -1, 1], [-1, 1, 0]])
# q2 = np.arange(-11, 151, 10)
# rad = np.zeros((len(q2)))
# for i in range(len(q2)):
# 	radi = fast_ffs(q2[i], r)
# 	rad[i]= radi
# print("This program took ", time.time() - start_time2, "seconds to run.")
#
# start_time2 = time.time()
# r = np.array([[-1, -1, 1], [-1, 1, 0]])
# q2 = np.arange(-11, 151, 10)
# l1 = .267
# l2 = .272
# rad = np.zeros((len(q2)))
# for i in range(len(q2)):
# 	radi = ffs(0, q2[i], l1, l2, r, 1)
# 	rad[i]= radi
# print("This program took ", time.time() - start_time2, "seconds to run.")

