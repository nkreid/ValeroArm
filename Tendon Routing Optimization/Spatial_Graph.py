from FFS import ffs
import numpy as np
import matplotlib.pyplot as plt

l1 = .267
l2 = .272
r = np.array([[-1, -1, 1], [-1, 1, 0]])
q2 = np.arange(10, 150, 10)
for i in range(len(q2)):
    endpoint = ffs(0, q2[i], l1, l2, r, 1)[1]  # need to add "endpoint" as a return of ffs
    radi = ffs(0, q2[i], l1, l2, r, 1)[0]
    plt.plot(endpoint[0], endpoint[1], 'bo', ms=radi*10)
    plt.plot(endpoint[0], endpoint[1], 'ko')
    plt.plot([.267,endpoint[0]], [0,endpoint[1]], 'k-')

plt.plot(.267,0, 'ko')
plt.plot([0,.267], [0,0],'k-')
plt.xlabel('X-position')
plt.ylabel('Y-position')
plt.title('Max Force Output at Endpoints')

plt.show()

