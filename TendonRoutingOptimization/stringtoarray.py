import numpy as np
import pickle

def load_obj(name):
	with open('obj/' + name + '.pkl', 'rb') as f:
		return pickle.load(f)


def string2array(string):
	x = string.replace('[', '')
	x = x.replace(']', '')
	x = x.replace('\n', '')
	a = ' '.join(x.split())
	return np.fromstring(a, sep=' ')


def keys_return(my_dict):
	a = list(my_dict.keys())
	return a


def pkl2npy_file(pkl_file):
	best_array_list = []
	unpacked = load_obj(pkl_file)
	best_keys = keys_return(unpacked)
	for i in range(len(best_keys)):
		arr = string2array(best_keys[i])
		best_array_list.append(arr)
	best_routes = np.vstack(best_array_list)
	np.save(pkl_file, best_routes)

pkl2npy_file('best_routes')

a = load_obj('best_routes_step2')

# Create a list of tuples sorted by index 1 i.e. value field
listofTuples = sorted(a.items() ,  key=lambda x: x[1])

# Iterate over the sorted sequence
for elem in listofTuples :
	print(elem[0] , " ::" , elem[1]/160)
