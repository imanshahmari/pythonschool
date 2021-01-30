import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.sparse import csr_matrix

lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]

lc = LineCollection(lines, color=['k'])
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.add_collection(lc)
ax1.autoscale()

plt.show()