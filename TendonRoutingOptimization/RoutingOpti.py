import numpy as np
from scipy import integrate
import itertools
import os
import time
from heapq import nsmallest
from random import randint
import pprint
from fast_ffs import fast_ffs
from matplotlib import pyplot as plt
import pickle


def optiFFS(rout, angle_step):
    q2 = np.arange(-11, 151, angle_step)  # Bounds are physiological boundaries of elbow in degrees
    num_steps = len(q2)
    rad = np.zeros((1, num_steps))
    for i in range(len(q2)):
            rad[0, i] = fast_ffs(q2[i], rout)
    area = integrate.trapz(np.absolute(rad), x=q2)
    mean = area/num_steps
    return float(area)


# This function shows a graph that shows there is no dependence of the shoulder angle
# on the optimization parameter
def optiplot(rout):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    q1 = np.linspace(-40, 170, 15)
    q2 = np.linspace(-10, 150, 15)
    l1 = .267
    l2 = .272
    rad = np.zeros((len(q1), len(q2)))
    for i in range(len(q1)):
        for e in range(len(q2)):
            rad[i, e] = ffs(q1[i], q2[e], l1, l2, rout, 1)


    q1, q2 = np.meshgrid(q1, q2)
    ax.plot_surface(q1, q2, rad, linewidth=0, antialiased=False)

    # Plot formatting
    plt.xlabel('Shoulder Angle')
    plt.ylabel('Elbow Angle')
    plt.title('Max radius at given endpoint')
    plt.xlim(-40, 170)
    plt.ylim(-10, 150)
    plt.show()


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

# This function below is used to create the possible unscaled routes.
# np.save('PossibleRoutes',possible_routes(a,b))


def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def status_update(sample, percent_print):
    update = int(sample * percent_print/100)
    return update


def random_optimization(sample, angle_step, update, test_order):
    test_keys = list(range(100))
    top_dict = {el:0 for el in test_keys}
    for i in range(sample):
        route = np.array(data[test_order[i]]).reshape((2,3))
        try:
            f = optiFFS(route, angle_step)
        except:
            f = 0
        route_string = np.array2string(route)
        top_dict[route_string] = f
        worst_key = nsmallest(1, top_dict, key=top_dict.get)
        top_dict.pop(worst_key[0])
        if i % update == 0:
            print("You are " + str(i*Status_update_percent/update_freq) + " percent done.")
    return top_dict


def sequential_optimization(sample, angle_step, update):
    test_keys = list(range(100))
    top_dict = {el:0 for el in test_keys}
    for i in range(sample):
        route = np.array(data[i]).reshape((2,3))
        try:
            f = optiFFS(route, angle_step)
        except:
            f = 0
        route_string = np.array2string(route)
        top_dict[route_string] = f
        worst_key = nsmallest(1, top_dict, key=top_dict.get)
        top_dict.pop(worst_key[0])
        if i % update == 0:
            print("You are " + str(i*Status_update_percent/update_freq) + " percent done." )
            save_obj(top_dict, 'temp_top_routes')
    return top_dict


# Data from PossibleScaledRoutes.py
data = np.load(os.path.expanduser("~/Downloads/Normalized_Routes_v2.npy"))

# Optimization Parameters
sample = 1000                   # Max sample is len(data) = 4,348,472
Status_update_percent = 1      # Percentages to be notified at during process
angle_step = 20                 # Angle to step through in the optiFFS function
update_freq = status_update(sample, Status_update_percent)

# # Random Optimization
# random_1000 = np.random.randint(0, high=4348472, size=1000)
# start_time = time.time()
# best_routes = random_optimization(sample, angle_step, update_freq, random_1000)
# print("This program took ", time.time() - start_time, "seconds to run " + str(sample) +
#       " random matrices from the list.\n \nHere are the hundred best matrices:"
#       )
# # Create a list of tuples sorted by index 1 i.e. value field
# listofTuples = sorted(best_routes.items() ,  key=lambda x: x[1])
#
# # Iterate over the sorted sequence
# for elem in listofTuples :
#     print(elem[0] , " ::" , elem[1] )


# Sequential Optimization
start_time2 = time.time()
best_routes = sequential_optimization(sample, angle_step, update_freq)
save_obj(best_routes, 'best_routes')
print("This program took ", time.time() - start_time2, "seconds to run " + str(sample) +
      " sequential matrices from the list.\n" +
      "\nHere are the hundred best matrices:")
# Create a list of tuples sorted by index 1 i.e. value field
listofTuples = sorted(best_routes.items() ,  key=lambda x: x[1])

# Iterate over the sorted sequence
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )

