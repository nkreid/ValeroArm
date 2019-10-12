import numpy as np
import itertools


# This function creates a list of possible steps
def scale_list(max_moment_arm, step):
	values = [0]
	x = 0
	for n in range(int(max_moment_arm/step)):
		x += step
		values.append(x)
	values = np.array(values)
	return values


def iterate_matrix(size, scales):
	flat_matrix = np.zeros(size).flatten()
	poss_matrices = list(itertools.product(scales.tolist(), repeat=len(flat_matrix)))
	# for n in range(len(poss_matrices)):
	# 	print(poss_matrices[n])
	return np.array(poss_matrices)


# This function takes in unscaled routes, and their scaling matrices, and outputs a 3d array of all possibilities
def scaled_routes(possible_routes, scales):
	scaled_matrix_list = []
	for i in possible_routes:
		for n in range(len(iterate_matrix((2,3), scales))):
			scale_matrix = np.array((iterate_matrix((2,3), scales)[n]))
			new_matrix = i * scale_matrix.reshape((2,3))
			scaled_matrix_list.append(new_matrix)
	new_matrix_3d = np.stack(scaled_matrix_list)
	return new_matrix_3d


def save_routes(name, routes):
	np.save(name, routes)

# np.set_printoptions(threshold=np.sys.maxsize)  # Prints un-truncated arrays

# Parameters for scaling, Maximum moment arm of 1 implies all values are normalized by the largest moment arm
Scales = scale_list(1, 0.1)

# Possible unscaled routes from prior code
unscaled_routes = np.load('PossibleRoute.npy')

scaled_routes = scaled_routes(unscaled_routes, Scales)

save_routes('Normalized_Routes', scaled_routes)


