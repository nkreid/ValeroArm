from FFS import ffs
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = np.array([[-1, 1, -1], [1, 0, -1]])

q1 = np.arange(5, 50, 10)
q2 = np.arange(5, 50, 10)
l1 = .267
l2 = .272
rad = np.zeros((len(q1), len(q2)))
for i in range(len(q1)):
    for e in range(len(q2)):
        rad[i, e] = ffs(q1[i], q2[e], l1, l2, r, 1)


q1, q1 = np.meshgrid(q1, q2)
ax.plot_surface(q1, q2, rad,
                       linewidth=0, antialiased=False)

plt.xlabel('Elbow Angle')
plt.ylabel('Shoulder Angle')
plt.title('Max radius at given endpoint')
plt.show()

