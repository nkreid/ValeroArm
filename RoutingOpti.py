import numpy as np
import itertools
from OptiFFS import optiFFS

# This function produces possible rows with specified possibilities
def poss_rows(value_list, length):
    row = np.array(list(itertools.product(value_list, repeat=length)))
    row_del = []
    for i in range(len(row)):
        if -1 in row[i] and 1 in row[i]:
            pass
        else:
            row_del.append(i)
    row = np.delete(row, row_del, 0)
    return row

# This function combines rows and removes matrices if they are
# different rearrangements of columns
def possible_routes(row1,row2):
    poss_list = []
    for i in row1:
        for j in row2:
            route = np.array([i, j])
            arr = route[:,np.lexsort((route[1,:], route[0,:]))]
            if not any((arr == x).all() for x in poss_list):
                poss_list.append(arr)
    return np.asarray(poss_list)

# There cant be a column the has a zero above a non-zero value this is because tendons
# can not pass a distal joint without first passing the ones proximal to it
a = poss_rows([-1, 1], 3)
b = poss_rows([-1, 0, 1], 3)

data = np.load('PossibleRoute.npy')
dicts = {}
routes = []
radii = []
for i in data[1:]:
    try:
        f = optiFFS(i)
    except QhullError:
        pass
    routes.append(i)
    radii.append(f)
    print(routes)
    print(np.asarray(radii))

