from FFS import ffs
import numpy as np

r = np.array([[-1, 1, -1], [1, 0, -1]])

q1 = np.arange(45, 90, 1)
q2 = np.arange(45, 90, 1)
l1 = .267
l2 = .272
# r_list = []
# for i in range(len(q1)):
#     (ffs(q1[i], 90, l1, l2, r, 1, 'N'))
#
# print(r_list)

f = ffs(q1, q2, l1, l2, r, 1, 'N')

fig, ax = plt.subplots()

s = ax.scatter(q1, q2, c=f)
fig.colorbar(s)
plt.show()

