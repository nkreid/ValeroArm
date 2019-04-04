import numpy as np
import itertools


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

a = poss_rows([-1, 1], 3)
b = poss_rows([-1, 0, 1], 3)

poss = np.array([[[]]])
for i in a:
    for j in b:
        route = np.array([i, j])
        arr = route[:,np.lexsort((route[1,:], route[0,:]))]
        print(arr)


