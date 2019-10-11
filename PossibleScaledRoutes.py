from FFS import ffs
import numpy as np
from OptiFFS import optiFFS
import itertools


def possible_matrix_values(max, step):
	values = [0]
	x = 0
	for n in range(int(max/step)):
		x += step
		values.append(x)
	values = np.array(values)
	return values


def iterate_matrix(size, values):
	flat_matrix = np.zeros(size).flatten()
	poss_matrices = list(itertools.product(values.tolist(), repeat=len(flat_matrix)))
	# for n in range(len(poss_matrices)):
	# 	print(poss_matrices[n])
	return np.array(poss_matrices)

poss_values = possible_matrix_values(1, 0.2)

np.set_printoptions(threshold=np.sys.maxsize)  # Prints un-truncated arrays

routes = np.load('PossibleRoute.npy')
for i in routes:
	for n in range(len(iterate_matrix((2,3), poss_values)[0:10])):
		scale_matrix = np.array((iterate_matrix((2,3), poss_values)[20000+n]))
		new_matrix = i* scale_matrix.reshape((2,3))
		print(new_matrix)
# routes = []
# radii = []
# for i in data:
#     try:
#         f = optiFFS(i)
#     except:
#         f = 'Error'
#     routes.append(i)
#     radii.append(f)
# print(routes)
# print(radii)
