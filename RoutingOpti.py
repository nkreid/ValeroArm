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


