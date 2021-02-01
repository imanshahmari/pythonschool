from HW1v2 import *
import itertools

path = list(itertools.chain(*zip(path,path)))
del path[1]
del path[len(path)-1]
path = np.array(path)
path = np.reshape(path,(int(len(path)/2), 2))

L_path = []
for i in range(0, len(path)):
    cc_path = []
    for j in range(0, len(path[1, :])):
        cc_path.append(tuple(coordinates[path[i, j]]))
    L_path.append(cc_path)

L = []
for i in range(0, len(indices)):
    cc = []
    for j in range(0, len(indices[1, :])):
        cc.append(tuple(coordinates[indices[i, j]]))
    L.append(cc)

lc = LineCollection(L, color=['k'],linewidth=0.5)
lc1 = LineCollection(L_path, color=['r'])

fig = plt.figure()
ax = fig.gca()
ax.add_collection(lc)
ax.add_collection(lc1)
ax.autoscale()
plt.scatter(coordinates[:,0], coordinates[:,1], label='y-values')
plt.xlabel('$x$')
plt.legend()


