import numpy as np
import time

def LargestCircle(hul, x_center, y_center):
	space = np.linspace(0, 2*np.pi)
	circ = np.array([np.cos(space), np.sin(space)])
	r = 0
	step = 0.0005
	inHull = True
	num_iterations = 0
	while inHull == True:

		points = (r* circ) + np.array([x_center, y_center])

		from scipy.spatial import Delaunay
		if not isinstance(hul, Delaunay):
			hull = Delaunay(hul)
		if np.all(hull.find_simplex(points.T)>=0):
			r += step
			num_iterations += 1
		else:
			break
	print(r)
	return r, points


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

	# max_R, circle = LargestCircle(W.T, endpoint[0], endpoint[1])
	max_R = 1
	return max_R

start_time2 = time.time()
r = np.array([[-1, -1, 1], [-1, 1, 0]])
q2 = np.arange(-11, 151, 10)
rad = np.zeros((len(q2)))
for i in range(len(q2)):
	radi = fast_ffs(q2[i], r)
	rad[i]= radi
	print(rad)
print("This program took ", time.time() - start_time2, "seconds to run.")

