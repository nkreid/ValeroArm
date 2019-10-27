import numpy as np
import itertools


def iterate_matrix(size, scales):
	flat_matrix = np.zeros(size).flatten()
	poss_matrices = list(itertools.product(scales.tolist(), repeat=len(flat_matrix)))
	return np.array(poss_matrices)


# This function takes in unscaled routes, and their scaling matrices, and outputs a 2d array of all possibilities
def scaled_routes(possible_routes, scales):
	scaled_matrix_list = []
	poss_scales = iterate_matrix((2,3), scales)
	row_mask = (poss_scales == 1.).any(axis=1) # This removes all matrices without a 1, a one is needed for normalizations
	reduced_scales = poss_scales[row_mask,:]
	for i in possible_routes:
		x = i.flatten() * reduced_scales
		x_unique, idx = np.unique(x, return_index = True, axis =0)
		scaled = x_unique[idx.argsort()]
		scaled_matrix_list.append(scaled)
	routes = np.vstack(scaled_matrix_list)
	return routes

def save_routes(name, routes):
	np.save(name, routes)

# np.set_printoptions(threshold=np.sys.maxsize)  # Prints un-truncated arrays

# Parameters for scaling, Maximum moment arm of 1 implies all values are normalized by the largest moment arm
Scales = np.arange(0.1, 1.1, .1)

# # Possible unscaled routes from prior code
unscaled_routes = np.load('PossibleRoutes.npy')

scaled_routes = scaled_routes(unscaled_routes, Scales)

save_routes('Normalized_Routes', scaled_routes)


